from django.urls import path
from menu3 import views

urlpatterns = [
    #การประชุม
    path('meeting/', views.event_1, name='meeting'),
    path('meeting/<int:meeting_id>', views.event1_detail, name='meeting_detail'),
    path('register/meeting/', views.event1_register, name='event1_register'),

    #การฝึกอบรม
    path('training/', views.event_2, name='training'),
    path('training/<int:training_id>', views.event2_detail, name='training_detail'),
    path('register/training/', views.event2_register, name='event2_register'),
    
    #การสัมมนา
    path('seminar/', views.event_3, name='seminar'),
    path('seminar/<int:seminar_id>', views.event3_detail, name='seminar_detail'),
    path('register/seminar/', views.event3_register, name='event3_register'),
    
    #การเสวนา
    path('converse/', views.event_4, name='converse'),
    path('converse/<int:converse_id>', views.event4_detail, name='converse_detail'),
    path('register/converse/', views.event4_register, name='event4_register'),
]