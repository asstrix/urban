from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, BooleanField, FileField, ColorField
from wtforms.validators import DataRequired, Length, EqualTo, Email, NumberRange
from flask_wtf.file import FileAllowed


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=3, max=15)])
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password', message="Passwords must match")])
    submit = SubmitField('Sign up')


class QRCodeForm(FlaskForm):
    data = StringField('URL', validators=[DataRequired(), Length(max=255)], render_kw={"placeholder": "Enter URL..."})
    size = IntegerField('QR code Size (1-40)', validators=[DataRequired(), NumberRange(min=1, max=40)])
    transparent = BooleanField('Transparent background')
    background = FileField('Custom background', validators=[FileAllowed(['jpg', 'png'], 'Images only!')])
    logo = FileField('Logo', validators=[FileAllowed(['jpg', 'png'], 'Images only!')])
    color = ColorField('Color', default='#ff0000')
    submit = SubmitField('Create')
    reset = SubmitField('Reset')
