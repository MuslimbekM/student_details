import random

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from firebase_admin import firestore

db = firestore.client()

from django.shortcuts import render, redirect

import uuid

# Talaba ID generatsiya qilish funktsiyasi
def generate_student_id():
    base_id = "380221103163"  # Asosiy ID qismi
    last_number = random.randint(1, 9)  # 1 dan 9 gacha bo'lgan raqam
    return f"{base_id}_{last_number}"

def add_student(request):
    if request.method == "POST":
        student_id = generate_student_id()
        create_date = request.POST.get('create_date', '')

        if not student_id:
            return render(request, 'add_student.html', {'error': 'Talaba ID kiritilishi shart!'})

        full_name = request.POST.get('full_name', '')
        birth_date = request.POST.get('birth_date', '')
        nationality = request.POST.get('nationality', '')
        education_type = request.POST.get('education_type', '')
        education_form = request.POST.get('education_form', '')
        admission_type = request.POST.get('admission_type', '')
        admission_year = request.POST.get('admission_year', '')
        university = request.POST.get('university', '')
        faculty = request.POST.get('faculty', '')
        specialization = request.POST.get('specialization', '')
        course = request.POST.get('course', '')

        student_data = {
            'studentId': student_id,
            'createDate': create_date,
            'full_name': full_name,
            'birth_date': birth_date,
            'nationality': nationality,
            'education_type': education_type,
            'education_form': education_form,
            'admission_type': admission_type,
            'admission_year': admission_year,
            'university': university,
            'faculty': faculty,
            'specialization': specialization,
            'course': course,
        }

        db.collection("students").document(student_id).set(student_data)

        return redirect(reverse('student_detail', kwargs={'student_id': student_id}))
    return render(request, 'add_student.html')


def student_detail(request, student_id):  # student_id argumentini qabul qiladi
    student_ref = db.collection("students").document(student_id)
    student = student_ref.get()

    if student.exists:
        return render(request, 'student_detail.html', {'student': student.to_dict()})
    else:
        return render(request, 'student_detail.html', {'error': 'Talaba topilmadi!'})


def home(request):
    return render(request, "home.html")
