from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

from students.views import home


def redirect_to_student_detail(request):
    return redirect('student_detail')  # student_detail sahifasiga yo‘naltirish


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', redirect_to_student_detail),  # Asosiy sahifa student_detail ga yo‘naltirildi
    path('student/', include('students.urls')),
    path('home/', home, name='home'),  # Bosh sahifa
]
