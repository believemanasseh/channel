from django.urls import path
from shop.views import *


urlpatterns = [
	path('', homepage, name='home'),
]