from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),  # Remove the space here
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
]