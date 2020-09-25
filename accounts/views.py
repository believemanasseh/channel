from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse
from django.views.generic import FormView
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from accounts.forms import CustomUserForm

def register_view(request):
	form = CustomUserForm()
	if request.method == "POST":
		form = CustomUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data['username']
			messages.success(request, "Account successfully created for {}!".format(user))
			return redirect('login')
		
	context = {'form': form}
	return render(request, 'registration/register.html', context)

"""
def login_view(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']

		# authenticate user
		user = authenticate(request, username=username, password=password)

		if user.is_active():
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, "Oops... Incorrect login credentials!")

	context = {}
	return render(request, 'registration/login.html', context)
"""
'''
def logout_user(request):
	logout(request)
	return redirect('login')
'''
