from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import *
from django.db.models import Avg
from userauth.models import *
from .forms import CommentForm
from django.contrib.auth import logout,login,authenticate
#from userauth.models import User

def home(request):
	all_teachers = TeacherProfile.objects.all()
	all_comments = CommentSection.objects.all()
	avg_stars = all_comments.aggregate(Avg('stars'))

	context = {"at":all_teachers}	

	return render(request,'index.html',context)

def profile(request,sname):
	teacher = get_object_or_404(TeacherProfile,s_name = sname)
	all_comments = CommentSection.objects.filter(Teacher = teacher)
	avg_stars = all_comments.aggregate(Avg('stars'))
	if avg_stars['stars__avg'] is not None:
		avg_stars['stars__avg'] = round(avg_stars['stars__avg'],2)
		
	if request.method == "POST":
		comment = CommentForm(request.POST)
		if comment.is_valid():
			comment = comment.save(commit = False)
			comment.Teacher = teacher
			comment.user = request.user
			comment.save()
			return redirect(f'/profile/{sname}')

	else:
		comment = CommentForm()
	context = {'teacher':teacher,'com':comment,'all_com':all_comments,'astar':avg_stars}

	return render(request,"profile.html",context)

def login_user(request):
	if request.method == 'POST':
		email = request.POST['email']
		passwd = request.POST['Password']
		print(email,passwd)
		user = authenticate(email = email,password = passwd)
		if user is not None:
			print('logged in!!')
			login(request,user)
			return redirect('/')
		else:
			print("not loggin in")
	return render(request,'login.html')

def logout_user(request):
	logout(request)
	return redirect('/')