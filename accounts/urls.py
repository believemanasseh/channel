from django.urls import path
from accounts.views import *

urlpatterns = [
	path('register/', register_view, name='register'),
]