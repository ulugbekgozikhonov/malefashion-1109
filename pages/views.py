from django.shortcuts import render
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

	context = {
		"products": products
	}

	return render(request, "shop.html", context)


def blog_view(request):
	return render(request, 'blog.html')


def contact_view(request):
	return render(request, 'contact.html')


def about_view(request):
	return render(request, 'about.html')
