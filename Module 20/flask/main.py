from flask import Flask, render_template, redirect, flash, session, request, send_file, url_for
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from forms import LoginForm, RegisterForm, QRCodeForm
from io import BytesIO
from PIL import Image
import qrcode, base64

app = Flask(__name__)
app.secret_key = 'X^h9k9rWW6n2Q1P5'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = None


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=False, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


class QRCode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    qrcode_data = db.Column(db.LargeBinary, nullable=False)
    name = db.Column(db.String(255), nullable=False)

    user = db.relationship('User', backref=db.backref('qrcodes', lazy=True))


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/', methods=['GET', 'POST'])
@login_required
def index():
    form = QRCodeForm()
    if form.validate_on_submit():
        try:
            data = form.data.data
            size = form.size.data
            transparent = form.transparent.data
            background = form.background.data
            logo = form.logo.data
            color = form.color.data
            qr = qrcode.QRCode(
                version=size,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(data)
            qr.make(fit=True)
            if background:
                back_color = "transparent"
            else:
                if transparent:
                    back_color = "transparent"
                else:
                    back_color = "black" if color == "#ffffff" else "white"
            img = qr.make_image(
                fill_color=color,
                back_color=back_color
            ).convert("RGBA")
            if background:
                background_image = Image.open(background).convert("RGBA")
                background_image = background_image.resize(img.size)
                img = Image.alpha_composite(background_image, img)
            if logo:
                logo_image = Image.open(logo).convert("RGBA")
                qr_width, qr_height = img.size
                logo_size = int(min(qr_width, qr_height) * 0.2)
                logo_image = logo_image.resize((logo_size, logo_size), Image.LANCZOS)
                logo_image.putalpha(200)  # Прозрачность логотипа
                logo_position = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)
                img.paste(logo_image, logo_position, logo_image)
            buffer = BytesIO()
            img.save(buffer, format="PNG")
            buffer.seek(0)
            qr_code_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
            qr_code_data = f"data:image/png;base64,{qr_code_base64}"
            new_qr = QRCode(user_id=current_user.id, qrcode_data=buffer.getvalue(), name=data)
            db.session.add(new_qr)
            db.session.commit()
            return render_template("main.html", form=form,  user=current_user.name, qr_code=qr_code_data, qr_code_id=new_qr.id)
        except Exception as e:
            return render_template("main.html", form=form, user=current_user.name, error=f"Error generating QR code: {e}")
    return render_template("main.html", form=form, user=current_user.name)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(email=email).first()
        if user and user.password == password:
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password.', 'danger')
    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    session.pop('_flashes', None)
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        email = form.email.data
        name = form.name.data
        password = form.password.data

        user_exists = User.query.filter_by(email=email).first()
        if user_exists:
            flash('User already exists.', 'danger')
        else:
            new_user = User(name=name, email=email, password=password)
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful. Please log in.', 'success')
            return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/qrcodes')
@login_required
def qrcodes():
    user_qrcodes = QRCode.query.filter_by(user_id=current_user.id).all()
    return render_template('qrcodes.html', user=current_user.name, codes=user_qrcodes)


@app.route('/download/<int:qr_code_id>')
def qr_download(qr_code_id):
    qr_code = QRCode.query.get_or_404(qr_code_id)
    qr_code_name = qr_code.name.replace('https://', '')
    return send_file(BytesIO(qr_code.qrcode_data), mimetype='image/png', as_attachment=True, download_name=f"{qr_code_name}.png")


@app.route('/delete/<int:qr_code_id>', methods=['POST'])
def qr_delete(qr_code_id):
    qr_code = QRCode.query.get_or_404(qr_code_id)
    db.session.delete(qr_code)
    db.session.commit()
    return redirect(url_for('qrcodes'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
