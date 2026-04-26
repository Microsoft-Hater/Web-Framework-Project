from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout

# Create your views here.

def homeView(request):
	if(request.user is not None):
		group = ""
		if(request.user.groups.filter(name="students").exists()):
			group = "Student"
		elif(request.user.groups.filter(name="lecturers").exists()):
			group = "Lecturer"
		elif(request.user.groups.filter(name="helpdesk").exists()):
			group = "Help Desk Employee"
		return render(request, "services/home.html", {"user" : request.user, "group" : group})
	else:
		return render(request, "services/home.html")

def loginView(request):
	if request.method == "POST":
		username = request.POST.get("username")
		password = request.POST.get("password")

		user = authenticate(username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect("../")
		else:
			return render(request, "services/login.html", {"error": "Username Or Password Is Incorrect"})
	else:
		return render(request, "services/login.html")

def logoutView(request):
	logout(request)
	return redirect("../")