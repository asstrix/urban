import qrcode, time
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm, QRCodeForm
from io import BytesIO
from PIL import Image
import base64


def reg_page(request):
    title = 'QRBox: Register'
    context = {'title': title}
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    context['form'] = form
    return render(request, 'register.html', context)


def main_page(request):
    title = 'QRBox'
    context = {'title': title}
    if request.method == 'POST':
        form = QRCodeForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data['data']
            size = form.cleaned_data['size']
            color = form.cleaned_data['color']
            transparent = form.cleaned_data['transparent']
            logo = form.cleaned_data.get('logo')
            background = form.cleaned_data.get('custom_background')

            # Генерация QR-кода
            qr = qrcode.QRCode(
                version=size,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(data)
            qr.make(fit=True)

            # Создание изображения QR-кода
            img = qr.make_image(
                fill_color=color,
                back_color="transparent" if transparent else "white"
            )

            # Обработка пользовательского фона (если он был загружен)
            if background:
                try:
                    background_image = Image.open(background).convert("RGBA")

                    # Опционально: измените размер фонового изображения, чтобы оно совпадало с QR-кодом
                    background_image = background_image.resize(img.size)

                    # Объединение фонового изображения с QR-кодом
                    img = img.convert("RGBA")  # Перевод QR-кода в режим RGBA
                    background_image = background_image.convert("RGBA")

                    # Накладываем QR-код на фон
                    combined_img = Image.alpha_composite(background_image, img)
                    img = combined_img  # Используем изображение с фоном как результат
                except Exception as e:
                    context['result'] = f"Failed to set background: {e}"

            # Добавление логотипа (если был загружен)
            if logo:
                try:
                    logo_image = Image.open(logo).convert("RGBA")
                    img = img.convert("RGBA")
                    qr_width, qr_height = img.size
                    logo_size = int(min(qr_width, qr_height) * 0.2)
                    logo_image = logo_image.resize((logo_size, logo_size), Image.LANCZOS)
                    logo_position = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)
                    img.paste(logo_image, logo_position, logo_image)
                except Exception as e:
                    context['result'] = f"Failed to add logo: {e}"

            # Сохранение QR-кода в поток байтов
            buffer = BytesIO()
            img.save(buffer, format="PNG")
            buffer.seek(0)

            # Сохранение файла с уникальным именем
            qr_code = base64.b64encode(buffer.getvalue()).decode('utf-8')
            qr_code = f"data:image/png;base64,{qr_code}"
            context['result'] = 'Your QR Code'
            context['qr_code'] = qr_code
            return render(request, 'qr.html', context)

    else:
        form = QRCodeForm()

    context['form'] = form

    return render(request, 'main.html', context)



