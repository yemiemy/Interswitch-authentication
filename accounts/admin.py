from django.contrib import admin
from .models import EmailConfirmed, Role 
# Register your models here.



admin.site.register(EmailConfirmed)
admin.site.register(Role)