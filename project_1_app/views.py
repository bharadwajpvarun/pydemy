from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required



def login(response):
	return render(response,'login.html')

def signup(response):
	if response.method == 'POST':
		form = UserRegisterForm(response.POST)
		if form.is_valid():
			form.save(commit=True)
			username = form.cleaned_data.get('username')
			messages.success(response, f'YooHooo new user @{username} !')
			return redirect('login')
	else:
	    form = UserRegisterForm()
	return render(response, "signup.html", {'form': form})


@login_required
def pydemy(response):
	return render(response, "homePage.html")
