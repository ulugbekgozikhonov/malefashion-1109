from django.urls import path

from products.views import add_to_cart_view

app_name = "products"

urlpatterns = [
	path("add-to-cart/<int:pk>", add_to_cart_view, name="add-to-cart")

]
