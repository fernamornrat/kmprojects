from django.urls import path
from menu2 import views

urlpatterns = [
    ################## ฟิสิกส์ ##########################
    path('physic/', views.physic, name='physic'),
    path('physic/detail/<int:physics_id>', views.physic_detail, name='physic_detail'),

    ################## เคมี ############################
    path('chemistry/', views.chemistry, name='chemistry'),
    path('chemistry/detail/<int:chemistry_id>', views.chemistry_detail, name='chemistry_detail'),

    ################## ชีววิทยา ############################
    path('biology/', views.biology, name='biology'),
    path('biology/detail/<int:biology_id>', views.biology_detail, name='biology_detail'),
    
    ################## โครงงานวิทยาศาสตร์ ############################
    path('science/', views.science, name='science'),
    path('science/detail/<int:science_id>', views.science_detail, name='science_detail'),
]