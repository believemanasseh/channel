from django.urls import path
from shop.views import *

app_name = 'shop'

urlpatterns = [
	path('', HomepageView.as_view(), name='home'),
	path('products/', ProductsView.as_view(), name='products'),
	path('checkout/', CheckoutView.as_view(), name='checkout'),
]