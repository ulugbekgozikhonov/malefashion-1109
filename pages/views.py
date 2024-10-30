from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, DeleteView, UpdateView

from .models import Banner
from products.models import *


# def home_view(request):
# 	banners = Banner.objects.filter(status=True).all()
# 	context = {
# 		"banners": banners
# 	}
# 	return render(request, "index.html", context)


class HomeView(ListView):
	model = Banner
	template_name = "index.html"
	context_object_name = "banners"

	def get_queryset(self):
		return Banner.objects.filter(status=True).all()


def shop_view(request):
	products = Product.objects.order_by("-created_at")
	categories = Category.objects.order_by("-created_at")
	brands = Brand.objects.order_by("-created_at")
	colors = Color.objects.all()
	sizes = Size.objects.all()
	tags = Tag.objects.all()
	context = {
		"products": products,
		"categories": categories,
		"brands": brands,
		"colors": colors,
		'sizes': sizes,
		"tags": tags,
	}

	return render(request, "shop.html", context)


def blog_view(request):
	return render(request, 'blog.html')


def contact_view(request):
	return render(request, 'contact.html')


def about_view(request):
	return render(request, 'about.html')


def shop_detail_view(request, pk):
	product = Product.objects.filter(id=pk).first()

	context = {
		"product": product
	}
	return render(request, "shop-details.html", context)
