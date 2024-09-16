from fastapi import FastAPI, Request, APIRouter, Request, Form, File, UploadFile
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.templating import Jinja2Templates
import qrcode
from io import BytesIO
from PIL import Image

router = APIRouter(prefix="/qrcodes", tags=["qrcodes"])
templates = Jinja2Templates(directory="templates")


@router.post("/create")
async def create_qr_code(
		request: Request,
		data: str = Form(...),
		size: int = Form(...),
		transparent: bool = Form(False),
		background: UploadFile = File(None),
		logo: UploadFile = File(None),
		color: str = Form("#ff0000")
):
	# Создание базового QR-кода
	qr = qrcode.QRCode(
		version=1,  # версия 1 означает маленький размер, но адаптируется в зависимости от данных
		error_correction=qrcode.constants.ERROR_CORRECT_H,
		box_size=size,
		border=4,
	)

	# Добавляем данные в QR-код
	qr.add_data(data)
	qr.make(fit=True)

	# Создание изображения QR-кода
	img = qr.make_image(fill_color=color, back_color="white" if not transparent else None)

	# Если есть пользовательский фон, то накладываем его
	if background:
		background_image = Image.open(BytesIO(await background.read()))
		background_image = background_image.convert("RGBA")
		img = img.convert("RGBA")
		img = Image.alpha_composite(background_image, img)

	# Если есть логотип, то вставляем его в центр QR-кода
	if logo:
		logo_image = Image.open(BytesIO(await logo.read()))
		logo_image = logo_image.convert("RGBA")
		logo_size = (img.size[0] // 4, img.size[1] // 4)  # Логотип 25% размера QR-кода
		logo_image.thumbnail(logo_size)

		# Вставка логотипа в центр
		pos = ((img.size[0] - logo_image.size[0]) // 2, (img.size[1] - logo_image.size[1]) // 2)
		img.paste(logo_image, pos, mask=logo_image)

	# Создание ответа с изображением QR-кода
	img_byte_arr = BytesIO()
	img.save(img_byte_arr, format="PNG")
	img_byte_arr.seek(0)

	return StreamingResponse(img_byte_arr, media_type="image/png")