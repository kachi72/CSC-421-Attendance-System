from django.contrib import messages
from django.shortcuts import render, redirect
from .models import *


def landing_page(request):
    return render(request, 'home.html')


def home(request):
    # if a form is being submitted
    if request.method == 'POST':
        name = request.POST['name']
        faculty = request.POST['faculty']
        department = request.POST['department']
        student_number = request.POST['studentNumber']

        # Validate info received in the form
        if not all([name, faculty, department, student_number]):
            messages.error(request, 'All fields are required.')
            return render(request, 'register.html')

        # Check if the student already exists with the student number
        if Student.objects.filter(studentNumber=student_number).exists():
            messages.error(request, 'Student number already exists.')
            return render(request, 'register.html')

        # Create and save student information after validation
        try:
            student = Student.objects.create(
                name=name,
                faculty=faculty,
                department=department,
                studentNumber=student_number
            )
            return redirect('attendance')

        except Exception as e:
            messages.error(request, f'Error during registration: {str(e)}')
            return render(request, 'register.html')

    if request.method == 'GET':
        return render(request, 'register.html')


def attendance(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'attendance.html', context)


def student(request, pk):
    # if it is a delete request
    if request.method == 'POST':
        student = Student.objects.get(id=int(pk))
        student.delete()
        students = Student.objects.all()
        context = {'students': students}
        return render(request, 'attendance.html', context)
    students = Student.objects.get(id=int(pk))
    context = {'student': students}
    return render(request, 'student.html', context)
