from django.urls import path

from . import views

urlpatterns = [
	path("", views.homeView, name="index"),
	path("login/", views.loginView, name="login"),
	path("logout/", views.logoutView, name="logout"),
	path("fees/", views.feesView, name="fees"),
	path("grades/", views.gradesView, name="grades"),
	path("tickets/", views.ticketsView, name="tickets"),
	path("payFee/<int:feeid>", views.payFee, name="payFee"),
	path("createTicket/", views.createTicket, name="createTicket"),
	path("createGrade/", views.createGrade, name="createGrade"),
	path("updateTicket/<int:ticketid>", views.updateTicket, name="updateTicket"),
	path("updateGrade/<int:gradeid>", views.updateGrade, name="updateGrade"),
	path("updateFee/<int:feeid>", views.updateFee, name="updateFee"),
]
