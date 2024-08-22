from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
	list_display = ('name', 'balance', 'age')
	search_fields = ('name',)
	list_filter = ('age',)


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
	list_display = ('title', 'cost', 'size')
	search_fields = ('title',)
	list_filter = ('cost',)