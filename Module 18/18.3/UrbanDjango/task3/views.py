from django.shortcuts import render


# Create your views here.
def main_page(request):
	title = 'F&F rent a car'
	context = {
		'title': title
	}
	return render(request, 'third_task/main.html', context)


def order_page(request):
	title = 'Orders: F&F rent a car'
	context = {
		'title': title
	}
	return render(request, 'third_task/order.html', context)


def catalog_page(request):
	title = 'Catalog: F&F rent a car'
	context = {
		'title': title
	}
	return render(request, 'third_task/catalog.html', context)