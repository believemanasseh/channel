from django.shortcuts import render
from django.http import HttpResponse

from . import models

def homepage(request):
	return render(request, 'shop/homepage.html')
