from django.conf.urls import patterns, url

from cycleoholic import views

urlpatterns = patterns('',
	#url(r'/<username>/^$', views.store, name='store')
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contacts/$', views.contacts, name='contacts'),

	url(r'^login/$', views.user_login, name='login'),
	url(r'^logout/$', views.user_logout, name='logout'),
	url(r'^register/$', views.register, name='register'),
	url(r'^create_store/$', views.create_store, name='create_store'),	

	url(r'^addProduct/$', views.addProduct, name='addProduct'),
	url(r'^filter/$', views.filter, name='filter'),
	url(r'^store/(?P<store_id>\w+)/(?P<product_type>\w+)/$', views.inventory, name='inventory'),
	url(r'^(?P<product_id>\w+)/review$', views.review, name='review'),
)