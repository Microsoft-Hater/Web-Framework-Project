from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Fee(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=32)
	amount = models.DecimalField(max_digits=6, decimal_places=2)
	status = models.CharField(max_length=6, choices=[('Unpaid', 'Unpaid'), ('Paid', 'Paid')], default='Unpaid')
	date = models.DateTimeField(auto_now_add=True)

class Result(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	subject = models.CharField(max_length=32)
	grade = models.CharField(max_length=1)
	percentage = models.IntegerField()

class Ticket(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=200)
	status = models.CharField(max_length=11, choices=[('Open', 'Open'), ('In Progress', 'In Progress'), ('Resolved', 'Resolved')], default='Open')
	date = models.DateTimeField(auto_now_add=True)
