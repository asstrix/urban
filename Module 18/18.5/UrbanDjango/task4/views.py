from django.shortcuts import render


# Create your views here.
def main_page(request):
	title = 'F&F rent a car'
	header = 'Main Page'
	context = {
		'title': title,
		'header': header,
	}
	return render(request, 'fourth_task/main.html', context)


def order_page(request):
	title = 'Orders: F&F rent a car'
	header = 'Orders'
	context = {
		'title': title,
		'header': header,
	}
	return render(request, 'fourth_task/order.html', context)


def catalog_page(request):
	title = 'Catalog: F&F rent a car'
	header = 'Our cars'
	cars = ['Hyundai i30', 'Kia Stonic', 'Ford Focus', 'Skoda Scala', 'Ford Focus C-Max']
	context = {
		'title': title,
		'header': header,
		'cars': cars,
	}
	return render(request, 'fourth_task/catalog.html', context)