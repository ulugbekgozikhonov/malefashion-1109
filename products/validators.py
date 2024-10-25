from django.core.exceptions import ValidationError


def check_rating(value):
	if not (0 < value < 6):
		raise ValidationError("Rating must be between 1 and 5")