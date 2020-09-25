from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from .models import Product, Order

class HomepageView(ListView):
	model = Product
	template_name = 'homepage.html'

class ProductsView(ListView):
	model = Product
	template_name = 'products.html'

class CheckoutView(DetailView):
	model = Order
	template_name = 'checkout.html'
