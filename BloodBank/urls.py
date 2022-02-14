from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('register', views.register),
    path('login', views.login),
    path('contactus', views.contact),
    path('saveuser', views.saveuser),
    path('verifyuser', views.verifyuser),

    path('contact/',include('contact.urls')),
    path('myuser/',include('user.urls'))
]
