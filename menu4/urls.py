from django.urls import path
from menu4 import views

urlpatterns = [
    path('sumary', views.sumary, name='sumary'),
    ################### คอมเมนต์ #########################
    path('comment', views.comment, name='comment'),
    path('add/', views.add_comment, name='add_comment'),
]