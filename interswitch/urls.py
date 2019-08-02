"""interswitch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from accounts.views import register, dashboard, activation_view #, profile
from projects.views import createProject, projects, search
from teams.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('projects.urls')),
    path('', include('teams.urls'))
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "InterSwitch Admin"
admin.site.site_title = "InterSwitch Admin Portal"
admin.site.index_title = "Welcome to InterSwitch Portal"
