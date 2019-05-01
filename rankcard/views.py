from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect
from rankcard.controller import get_students, get_student_marks, create_student
from django.urls import reverse

def render_students(request):
    students = get_students()
    html = render_to_string('students.html', {'students': students})
    return HttpResponse(html)

def render_rankcard(request, id):
    marks = get_student_marks(id)
    html = render_to_string('marks.html', {'marks': marks, 'studentName': marks[0].student.name})
    return HttpResponse(html)

def render_student(request):
    html = render_to_string('student-info.html', {})
    return HttpResponse(html)

def create_student_details(request):
    name = request.POST.get('name')
    dob = request.POST.get('dob')
    address = request.POST.get('address')
    create_student(name, dob, address)
    return HttpResponseRedirect('/student/')