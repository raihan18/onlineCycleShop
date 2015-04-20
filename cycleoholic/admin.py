from django.contrib import admin
from cycleoholic.models import *
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
	"""docstring for ProductAdmin"""
	list_display=('product_name', 'store_owns', 'product_type', 'unit_price')

class ReviewAdmin(admin.ModelAdmin):
	"""docstring for ReviewAdmin"""
	list_display=('product', 'user', 'user_rating')		

admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Store)
admin.site.register(Purchase)
admin.site.register(Sell)