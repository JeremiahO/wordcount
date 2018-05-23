"""wordcount URL Configuration

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
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Where are users are directed if they go to the home page
    path('', views.homepage, name='home'),
    # Here we are creating another path but adding an extention to our webaddress 8000/eggs - EXAMPLE
    # path('eggs/', views.eggs)

    # Here we include the name name=count to reference in our html so our form know which url it is getting directed to
    path('counts/', views.count, name='count'),

    path('about/', views.aboutpage, name='about')


]
