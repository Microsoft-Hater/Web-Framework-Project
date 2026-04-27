from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from .models import Fee
from .models import Result
from .models import Ticket

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

@login_required
@permission_required("services.view_fee")
def feesView(request):
	allFees = Fee.objects.filter(user=request.user)

	filter = request.GET.get("status")
	if filter in ["Unpaid", "Paid"]:
		allFees = allFees.filter(status=filter)

	fees = allFees.order_by("-date")

	return render(request, "services/fee.html", {"fees": fees})

@login_required
@permission_required("services.view_result")
def gradesView(request):

	allGrades = ""
	isLecturer = False
	if(request.user.groups.filter(name="lecturers").exists()):
		allGrades = Result.objects.filter()
		isLecturer = True
	else:
		allGrades = Result.objects.filter(user=request.user)

	return render(request, "services/grades.html", {"grades": allGrades, "isLecturer": isLecturer})

@login_required
@permission_required("services.view_ticket")
def ticketsView(request):
	allTickets = Ticket.objects.filter(user=request.user)

	filter = request.GET.get("status")
	if filter in ["Open", "In Progress", "Resolved"]:
		allTickets = allTickets.filter(status=filter)

	tickets = allTickets.order_by("-date")

	return render(request, "services/tickets.html", {"tickets": tickets})

@login_required
@permission_required("services.change_fee")
def payFee(request, feeid):
	fee = Fee.objects.get(id=feeid)
	fee.status = "Paid"
	fee.save()
	return redirect("fees")

@login_required
@permission_required("services.add_ticket")
def createTicket(request):
	if request.method == "POST":
		title = request.POST.get("title")
		description = request.POST.get("description")

		Ticket.objects.create(user=request.user, title=title, description=description)

		return redirect("tickets")
	else:
		return render(request, "services/createTicket.html")