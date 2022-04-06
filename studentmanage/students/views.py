from urllib import request
from django.shortcuts import render, redirect
from student.form import stuForm
from student.function import handle_uploaded_file 
from student.models import student, degree, department, faculty, semester, subject
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.


def stu_login(request):
    if request.method == "POST": 
        e = request.POST["email"]
        p = request.POST["password"]
        print("+++++++++++++++++++++",e)
        val = student.objects.filter(email=e, password=p).count()

        if val == 1:
            val = student.objects.filter(email=e, password=p)
            print("+++++++++++++++++", val)
            for items in val:
                request.session['email'] = items.email
                return redirect("/students/show/")
        else:
            messages.error(request, "Invalid username and password")
            return render(request, "stu_login.html")
    else:
        pass

    return render(request, 'stu_login.html')


def show(request):
    d = degree.objects.all()
    s = subject.objects.all()
    return render(request, 'index1.html', {'d':d, 's':s})    


def header(request):
    return render(request, 'header1.html')


def degdet(request, id=0):
    d1 = department.objects.all()
    dep = department.objects.filter(deg_id_id=id)
    return render(request, 'degdet.html', {'dep':dep, 'd1':d1})


def detail(request, id=0):
    s = subject.objects.filter(dep_id_id=id)
    f = faculty.objects.filter(dep_id_id=id)
    print('----', f)
    return render(request, 'details.html', {'s':s, 'f':f})


def fac(request, id):
    f = faculty.objects.get(id=id)
    return render(request, 'fac.html', {'f':f})

def teacher(request):
    l = faculty.objects.all()
    return render(request, 'teacher.html', {'l':l})

                                         