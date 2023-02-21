from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.models import auth

def signup(request):
	if request.method =='POST':
		form = CustomUserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			em = request.POST['email']
			ps = request.POST['password1']
			user = auth.authenticate(email=em,password = ps)
			if user is not None:
				auth.login(request,user)
				print("avlo dhan pa...")
				return redirect('/')
	else:
		form = CustomUserCreationForm()


	context = {'form':form}

	return render(request,'signup.html',context)