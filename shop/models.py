from django.db import models
from django.conf import settings
from datetime import date
from accounts.models import CustomUser
from .constants import CATEGORY, STATUS

class Customer(models.Model):
	user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
	phone = models.CharField(max_length=20, null=True)
	city = models.CharField(max_length=100, null=True)
	state = models.CharField(max_length=100, null=True)
	date_of_birth = models.DateField(default=date.today)
	address1 = models.CharField(max_length=100, null=True)
	address2 = models.CharField(max_length=100, null=True)

	def __str__(self):
		return self.user.username

class Product(models.Model):
	name  = models.CharField(max_length=100, null=True)
	description = models.CharField(max_length=100, null=True, blank=True)
	category = models.CharField(max_length=100, null=True, choices=CATEGORY)
	price = models.FloatField(null=True)
	discount = models.FloatField(null=True)
	date_created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(null=True)

	def __str__(self):
		return self.name

class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	items = models.ManyToManyField(OrderItem)
	status = models.CharField(max_length=100, null=True, choices=STATUS)
	total_amount = models.FloatField(null=True)
	start_date = models.DateTimeField(auto_now_add=True, null=True)
	ordered_date = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.user.username

