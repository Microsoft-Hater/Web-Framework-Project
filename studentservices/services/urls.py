from django.urls import path

from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
	path("", views.homeView, name="index"),
	path("login/", views.loginView, name="login"),
]
