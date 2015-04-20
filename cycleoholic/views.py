from django.shortcuts import render
from django.http import *
from django.contrib.auth.models import User, Permission
from django.contrib.auth import authenticate, login, logout
from cycleoholic.models import *
from django.db.models import Avg

# Create your views here.
def home(request):
	return render(request, 'index.html')

def about(request):
	return render (request, 'about.html')

def contacts(request):
	return render (request, 'contacts.html')

def user_login(request):
	if request.method == "POST":
	    username = request.POST['username']
	    password = request.POST['password']
	    user = authenticate(username=username, password=password)
	    if user:
	    	if user.is_active:
	    		login(request, user)
	    		#permissions
	    		context= {'user': user}
	    		return render (request, 'index.html', context)
	return render(request, 'login.html')

def user_logout(request):
	logout(request)
	return render(request, 'index.html')

def register(request):
	if request.method == "POST":
		full_name = request.POST['full_name']
		username = request.POST['username']
		password = request.POST['password']
		email = request.POST['email']
		user = User.objects.create_user(username=username, password=password, first_name=full_name, email=email)
		user.save()
		user = authenticate(username=username, password=password)
		login(request, user)
		context={'user':user}
		return render (request, 'index.html', context)
	return render (request, 'register.html')

def create_store(request):
	confirmation=""
	if request.method == "POST":
		store_name=request.POST['store_name']
		username=request.POST['username']
		password=request.POST['password']
		# user = User.objects.get(username=username)
		# if user is None:
		user = User.objects.create_user(username=username, password=password, first_name=store_name)
		user.is_active=False
		user.save()
		permission = Permission.objects.get(name='Can add product')
		user.user_permissions.add(permission)
		permission = Permission.objects.get(name='Can change product')
		user.user_permissions.add(permission)		
		permission = Permission.objects.get(name='Can delete product')
		user.user_permissions.add(permission)

	context={'conf':confirmation}
	return render (request, 'create_store.html', context)

def addProduct(request):
	confirmation = ""
	if request.method=="POST":
		name=request.POST['name']
		product_type=request.POST['product_type']
		product_type=product_type.lower()
		price=request.POST['price']
		unit=request.POST['unit']
		details=request.POST['details']
		store=None
		if request.user.is_authenticated:
			store=User.objects.get(username=request.user.username)
		if not store is None:
			store.product_set.create(product_name=name, product_type=product_type, unit_price=price, unit_available=unit, product_details=details)
			confirmation = "true"
	context = {'conf':confirmation}
	return render (request, 'addProduct.html', context)

def inventory(request, store_id, product_type):
	store = User.objects.get(username=store_id)
	products= store.product_set.filter(product_type=product_type)
	context={'store':store, 'products':products}
	return render (request, 'storeInventory.html', context)

def filter(request):
	products= Product.objects.all()

	if request.method=="POST":
		null="null"
		store_id=request.POST['store']
		product_type=request.POST['product_type']
		product_type=product_type.lower()
		price_min=request.POST['price_min']
		price_min = int('0' + price_min)
		price_max=request.POST['price_max']
		maximum=99999999
		if store_id != null:
			products = products.filter(store_owns__username=store_id)
		if product_type != null:
			products = products.filter(product_type=product_type)
		products = products.filter(unit_price__gte=price_min)
		if price_max=="":
			products = products.filter(unit_price__lte=maximum)
		else:
			price_max=int('0'+price_max)
			products=products.filter(unit_price__lte=price_max)

	context={'products':products}
	return render (request, 'filter.html', context)

def review(request, product_id):
	product=Product.objects.get(pk=product_id)
	avg_rating=product.review_set.aggregate(Avg('user_rating')).values()[0]
	if request.method=="POST":
		review=request.POST['review']
		rating=request.POST['rating']
		product.review_set.create(user=request.user.username, user_review=review, user_rating=rating)
	reviews=product.review_set.all()
	context={'product':product, 'reviews':reviews, 'rating':avg_rating}
	return render (request, 'review.html', context)