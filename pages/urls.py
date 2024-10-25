from django.urls import path
from .views import HomeView, shop_view, blog_view, contact_view, about_view

app_name = "pages"

urlpatterns = [
	path("", HomeView.as_view(), name="home"),
	path("shop/", shop_view, name="shop"),
	path("blog/", blog_view, name="blog"),
	path("contact/", contact_view, name="contact"),
	path("about/", about_view, name="about"),

]
