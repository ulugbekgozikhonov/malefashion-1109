from django.shortcuts import render, redirect


def add_to_cart_view(request, pk):
	product_ids = request.session.get("cart", [])
	if pk in product_ids:
		product_ids.remove(pk)
	else:
		product_ids.append(pk)
	request.session["cart"] = product_ids
	print(product_ids)
	return redirect(request.META['HTTP_REFERER'])
