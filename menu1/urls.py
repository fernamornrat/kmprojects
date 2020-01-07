from django.urls import path
from menu1 import views

urlpatterns = [
    path('', views.index, name='index'),
    path('logout', views.logout, name='logout'),
]