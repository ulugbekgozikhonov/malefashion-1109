from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def signup_view(request):
	if request.method == "POST":
		username = request.POST.get("username")
		email = request.POST.get("email")
		password = request.POST.get("password")
		password_confirm = request.POST.get("password_confirm")
		if User.objects.filter(email=email).exists():
			messages.error(request, "This email already exists")
			return redirect(request.path_info)
		if User.objects.filter(username=username).exists():
			messages.error(request, "This username already taken")
			return redirect(request.path_info)
		if password and password_confirm and password != password_confirm:
			messages.error(request, "Passwords not match")
			return redirect(request.path_info)
		User.objects.create_user(
			username=username,
			password=password,
			email=email,
		)
		return redirect("users:login")
	return render(request, "registration/signup.html")


def login_view(request):
	if request.method == "POST":
		username = request.POST.get("username")
		password = request.POST.get("password")

		user = authenticate(request, username=username, password=password)
		if user:
			login(request, user)
			return redirect('pages:home')
		else:
			messages.error(request, "username or password error")

	return render(request, "registration/login.html")


def logout_view(request):
	logout(request)
	return redirect('pages:home')
