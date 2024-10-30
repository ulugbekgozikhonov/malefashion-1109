from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from PIL import Image


def check_rating(value):
	if not (0 < value < 6):
		raise ValidationError("Rating must be between 1 and 5")


@deconstructible
def validate_image_format(value):
	try:
		# Pillow kutubxonasidan foydalanib rasmni ochamiz
		img = Image.open(value)
		# Agar format PNG yoki JPEG bo'lmasa, xatolik qaytaramiz
		if img.format not in ['PNG', 'JPEG', 'HIEC', 'JPG']:
			raise ValidationError("Faqat PNG yoki JPEG formatdagi fayllarni yuklashingiz mumkin.")
	except Exception as e:
		raise ValidationError("Yaroqsiz rasm fayli.")
