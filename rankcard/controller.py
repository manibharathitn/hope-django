from rankcard.models import Student, Mark

def create_student(name, dob, address):
    student = Student()
    student.name = name
    student.dob = dob
    student.address = address
    student.save()

def create_mark(student_id, subject, mark):
    mark_obj = Mark()
    mark_obj.student = Student.objects.get(id=student_id)
    mark_obj.subject = subject
    mark_obj.mark = mark
    mark_obj.save()

def update_student(id, name, dob, address):
    student = Student.objects.get(id=id)
    student.name = name
    student.dob = dob
    student.address = address
    student.save()

def update_mark(student_id, subject, mark):
    mark_obj = Mark.objects.get(student_id=student_id, subject=subject)
    mark_obj.mark = mark
    mark_obj.save()

def get_student(id):
    student = Student.objects.get(id=id)
    return student

def get_student_marks(student_id):
    marks = Mark.objects.filter(student_id=student_id)
    return marks

def get_students():
    students = Student.objects.all()
    return students

def get_marks():
    marks = Mark.objects.all()
    return marks

