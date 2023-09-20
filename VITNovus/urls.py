"""
URL configuration for VITNovus project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from NovusApp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('index.html',views.index),
    path('supp.html',views.supp),
    path('register.html',views.register),
    path('reviews.html',views.reviews),
    path('arsan.html',views.arsan),
    path('buddys.html',views.buddys),
    path('cafe.html',views.cafe),
    path('canteen.html',views.canteen),
    path('enzo.html',views.enzo),
    path('foodcourt.html',views.foodcourt),
    path('hns.html',views.hns),
    path('onefood.html',views.onefood),
    path('quickbites.html',views.quickbites),
    path('onlineorder.html',views.onlineorder),
    path('save-input/', views.save_input_to_txt, name='save_input_to_txt')

]
