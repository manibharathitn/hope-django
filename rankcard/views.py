from django.template.loader import render_to_string
from django.http import HttpResponse
from rankcard.controller import get_students, get_student_marks

def render_students(request):
    students = get_students()
    html = render_to_string('students.html', {'students': students})
    return HttpResponse(html)

def render_rankcard(request, id):
    marks = get_student_marks(id)
    html = render_to_string('marks.html', {'marks': marks, 'studentName': marks[0].student.name})
    return HttpResponse(html)