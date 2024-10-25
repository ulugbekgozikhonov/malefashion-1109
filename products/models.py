from django.db import models
from .validators import check_rating
from general.models import BaseModel


class Category(BaseModel):
	title = models.CharField(max_length=31)

	def __str__(self):
		return self.title


class Brand(BaseModel):
	title = models.CharField(max_length=31)

	def __str__(self):
		return self.title


class Size(BaseModel):
	title = models.CharField(max_length=31)

	def __str__(self):
		return self.title


class Color(BaseModel):
	title = models.CharField(max_length=31)
	code = models.CharField(max_length=10)

	def __str__(self):
		return self.title


class Tag(BaseModel):
	title = models.CharField(max_length=31)

	def __str__(self):
		return self.title


class Product(BaseModel):
	name = models.CharField(max_length=31)
	description = models.TextField()
	price = models.FloatField()
	discount = models.FloatField()
	rating = models.PositiveIntegerField(validators=[check_rating], default=1)
	image = models.ImageField(upload_to="products/images/")
	category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
	brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="products")
	size = models.ManyToManyField(Size)
	color = models.ManyToManyField(Color)
	tag = models.ManyToManyField(Tag)

	def __str__(self):
		return self.name
