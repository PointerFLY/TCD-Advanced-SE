"""citymanage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from django.urls import path

from django.conf.urls import *
from django.contrib.auth import views as auth_views
from manager_dashboard import views as manager_dashboard_views

urlpatterns = [
    path('home/', manager_dashboard_views.home, name='home'),
    path('contact/', manager_dashboard_views.contact, name='contact'),
    path('login/', manager_dashboard_views.login, name='login'),
    path('index/', manager_dashboard_views.index, name='index'),
    path('monitor/', manager_dashboard_views.monitor, name='monitor'),
]
