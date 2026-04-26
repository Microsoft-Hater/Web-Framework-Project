from django.contrib import admin

from .models import Fee
from .models import Result
from .models import Ticket

# Register your models here.

admin.site.register(Fee)
admin.site.register(Result)
admin.site.register(Ticket)