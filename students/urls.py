from django.urls import path
from .views import student_detail, add_student, home

urlpatterns = [
    path('home/', home, name='home'),  # Bosh sahifa
    path('student/', student_detail, name='student_detail'),
    path('add_student/', add_student, name='add_student'),
    path('student/<str:student_id>/', student_detail, name='student_detail'),  # ID bilan ishlaydi
]
