from django.urls import path

from . import views

urlpatterns = [
	path("", views.homeView, name="index"),
	path("login/", views.loginView, name="login"),
	path("logout/", views.logoutView, name="logout"),
	path("fees/", views.feesView, name="fees"),
	path("grades/", views.gradesView, name="grades"),
	path("tickets/", views.ticketsView, name="tickets"),
]
