import qrcode, base64
from django.shortcuts import render, redirect
from .forms import LoginForm, SignUpForm, QRCodeForm
from django.contrib.auth.hashers import check_password
from io import BytesIO
from PIL import Image
from django.contrib import messages
from QRBox.models import Customer, QRCodes
from django.contrib.auth.hashers import make_password


def login_page(request):
    context = {'title': 'QRBox: Login'}
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            try:
                user = Customer.objects.get(email=email)
                if check_password(password, user.password):
                    request.session['user_id'] = user.id
                    context['user'] = user.name
                    context['form'] = QRCodeForm()
                    return render(request, "main.html", context)
                else:
                    messages.error(request, 'Invalid password.')
            except Customer.DoesNotExist:
                messages.error(request, 'User with this email does not exist.')
    else:
        context['form'] = LoginForm()
    context['form'] = LoginForm()
    return render(request, 'login.html', context)


def logout_view(request):
    request.session.flush()
    messages.success(request, 'You have been logged out.')
    return redirect('login')


def reg_page(request):
    context = {'title': 'QRBox: Register'}
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            name = form.cleaned_data.get('name')
            password = form.cleaned_data.get('password1')
            hashed_password = make_password(password)
            Customer.objects.create(email=email, name=name, password=hashed_password)
            messages.success(request, 'You have been successfully registered')
            context['form'] = LoginForm()
            return render(request, 'login.html', context)
        else:
            context['form'] = form
            return render(request, 'register.html', context)
    else:
        form = SignUpForm()
    context['form'] = form
    return render(request, 'register.html', context)


def main_page(request):
    context = {'title': 'QRBox'}
    user_id = request.session.get('user_id')
    if user_id:
        try:
            user = Customer.objects.get(id=user_id)
            context['user'] = user
        except Customer.DoesNotExist:
            request.session.flush()
            return redirect('login')
    else:
        return redirect('/')
    if request.method == 'POST':
        form = QRCodeForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data['data']
            size = form.cleaned_data['size']
            color = form.cleaned_data['color']
            transparent = form.cleaned_data['transparent']
            logo = form.cleaned_data.get('logo')
            background = form.cleaned_data.get('custom_background')
            qr_code, buffer, error = generate_qr_code(data, size, color, transparent, logo, background)
            if error:
                context['result'] = error
            else:
                context['result'] = 'Your QR Code'
                context['qr_code'] = qr_code
                QRCodes.objects.create(qrcode=buffer.getvalue(), q_name=data, user_id=user_id)
            return render(request, 'qr.html', context)
    else:
        form = QRCodeForm()
    context['form'] = form
    return render(request, 'main.html', context)


def qrcodes(request):
    context = {'title': 'QRBox: My QR codes'}
    user_id = request.session.get('user_id')
    if user_id:
        try:
            user = Customer.objects.get(id=user_id)
            context['user'] = user
        except Customer.DoesNotExist:
            request.session.flush()
            return redirect('login')
    else:
        return redirect('/')
    codes = QRCodes.objects.filter(user_id=user_id).values('id', 'q_name')
    print(list(codes))
    # for i in codes[0]:
    #     print(i)
    # context['codes'] = f"data:image/png;base64,{base64.b64encode(codes[0]['qrcode']).decode('utf-8')}"
    # context''
    return render(request, 'qrcodes.html', context)


def generate_qr_code(data, size, color, transparent, logo=None, background=None):
    try:
        qr = qrcode.QRCode(
            version=size,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(
            fill_color=color,
            back_color="transparent" if transparent else "white"
        )
        if background:
            background_image = Image.open(background).convert("RGBA")
            background_image = background_image.resize(img.size)
            img = img.convert("RGBA")
            background_image = background_image.convert("RGBA")
            img = Image.alpha_composite(background_image, img)
        if logo:
            logo_image = Image.open(logo).convert("RGBA")
            img = img.convert("RGBA")
            qr_width, qr_height = img.size
            logo_size = int(min(qr_width, qr_height) * 0.2)
            logo_image = logo_image.resize((logo_size, logo_size), Image.LANCZOS)
            logo_position = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)
            img.paste(logo_image, logo_position, logo_image)
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)
        qr_code = base64.b64encode(buffer.getvalue()).decode('utf-8')
        return f"data:image/png;base64,{qr_code}", buffer, None
    except Exception as e:
        return None,None, f"Error generating QR code: {e}"