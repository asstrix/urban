from django.shortcuts import render


# Create your views here.
def main_page(request):
	title = 'F&F rent a car'
	context = {
		'title': title
	}
	return render(request, 'fourth_task/main.html', context)


def order_page(request):
	title = 'Orders: F&F rent a car'
	context = {
		'title': title
	}
	return render(request, 'fourth_task/order.html', context)


def catalog_page(request):
	title = 'Catalog: F&F rent a car'
	context = {
		'title': title,
		'cars': ['Hyundai i30', 'Kia Stonic', 'Ford Focus', 'Skoda Scala', 'Ford Focus C-Max']
	}
	return render(request, 'fourth_task/catalog.html', context)