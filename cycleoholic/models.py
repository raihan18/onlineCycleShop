from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Store(models.Model):
	"""docstring for Store"""
	user = models.OneToOneField(User)
	store_address = models.CharField(max_length=200) 
	store_contact = models.CharField(max_length=15)

	def __str__(self):
		return self.user.username

class Product(models.Model):
	"""docstring for Product"""
	store_owns = models.ForeignKey(User)
	#product_id = models.CharField(max_length=10)
	product_type = models.CharField(max_length=10)
	product_name = models.CharField(max_length=30)

	unit_price = models.IntegerField(default=0)
	unit_available = models.IntegerField(default=0)

	product_details = models.CharField(max_length=2000)

	def __str__(self):
		return self.product_name


class Review(models.Model):
	"""docstring for review"""
	product = models.ForeignKey(Product)
	user = models.CharField(max_length=30) #reviewed by

	user_review = models.CharField(max_length=2000)
	user_rating = models.IntegerField(default=0)

	def __str__(self):
		return self.user # + "	" +
#		self.user_review + " || " + " Rating: "+ self.user_rating

class Purchase(models.Model):
	"""docstring for Purchase"""
	purchased_by = models.ForeignKey(User)
	purchased_from = models.ForeignKey(Store)
	#purchase_no = models.IntegerField(default=0) 

	purchased_products = models.CharField(max_length=2000)
	total_purchased_ammount = models.IntegerField(default=0)
	purchased_date = models.DateTimeField('date purchased')

	def __str__(self):
		return "Total ammount: "# + total_purchased_ammount

class Sell(models.Model):
	"""docstring for Sell"""
	customer = models.ForeignKey(User)
	seller = models.ForeignKey(Store)
	#sells_no = models.IntegerField(default=0)

	sold_products = models.CharField(max_length=2000)
	total_sold_ammount = models.IntegerField(default=0)
	sells_date = models.DateTimeField('date sold')

	def __str__(self):
		return "Total ammount: "# + total_sold_ammount
		