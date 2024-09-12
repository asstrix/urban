import qrcode, time
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm, QRCodeForm
from django.core.files.base import ContentFile
from io import BytesIO
from django.core.files.storage import default_storage
from django.conf import settings
from PIL import Image


def reg_page(request):
    title = 'QRBox: Register'
    context = {
        'title': title,
    }
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
    if request.method == 'POST':
        form = QRCodeForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data['data']
            size = form.cleaned_data['size']
            color = form.cleaned_data['color']
            transparent = form.cleaned_data['transparent']
            logo = form.cleaned_data.get('logo')
            custom_background = form.cleaned_data.get('custom_background')  # Получаем пользовательский фон
            options = form.cleaned_data['options']
            animated = form.cleaned_data['animated']

            # Генерация QR-кода
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=size,
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
            if custom_background:
                background_image = Image.open(custom_background)

                # Опционально: измените размер фонового изображения, чтобы оно совпадало с QR-кодом
                background_image = background_image.resize(img.size)

                # Объединение фонового изображения с QR-кодом
                img = img.convert("RGBA")  # Перевод QR-кода в режим RGBA
                background_image = background_image.convert("RGBA")

                # Накладываем QR-код на фон
                combined_img = Image.alpha_composite(background_image, img)
                img = combined_img  # Используем изображение с фоном как результат

            # Добавление логотипа (если был загружен)
            if logo:
                logo_image = Image.open(logo)
                logo_image.thumbnail((50, 50))  # Изменение размера логотипа
                img = img.convert("RGBA")
                img.paste(logo_image, (img.size[0] // 2 - 25, img.size[1] // 2 - 25), logo_image)

            # Сохранение QR-кода в поток байтов
            buffer = BytesIO()
            img.save(buffer, format="PNG")
            image_png = buffer.getvalue()

            # Сохранение файла с уникальным именем
            file_name = f'qr_code_{request.session.session_key}_{int(time.time())}.png'
            file_path = f'qr_codes/{file_name}'

            # Формирование URL для файла с уникальным параметром
            qr_code_url = settings.MEDIA_URL + file_path + f'?{int(time.time())}'

            context = {
                'qr_code_url': qr_code_url,
            }

            return render(request, 'main.html', context)

    else:
        form = QRCodeForm()

    context = {
        'form': form,
    }
    return render(request, 'main.html', context)


