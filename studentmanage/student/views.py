import sys

from django.contrib import messages
from django.shortcuts import render, redirect
from .form import degForm, depForm, stuForm, subForm, semForm, facForm, faForm, stForm
from .models import degree,department,student, semester, faculty, subject, user
from .function import handle_uploaded_file
# Create your views here.


def index(request):
    s = student.objects.all().count()
    f = faculty.objects.all().count()
    d = degree.objects.all().count()
    s = student.objects.all().count()
    return render(request, 'index.html', {'s':s, 'f':f, 'd':d, 's':s})


def addstu(request):
    d = degree.objects.all()
    d1 = department.objects.all()
    s = semester.objects.all()
    if request.method == "POST":
        form = stuForm(request.POST, request.FILES)
        print("--------", form.errors)
        if form.is_valid():
            try:
                handle_uploaded_file(request.FILES['image'])
                form.save()
                return redirect("/show_stu/")
            except:
                print("--------", sys.exc_info())
        else:
            pass
    else:
        form = facForm()
    return render(request, 'addStudent.html', {'s': s, 'd': d, 'd1': d1, 'form': form})


def addsem(request):
    d = degree.objects.all()
    d1 = department.objects.all()
    if request.method == "POST":
        form = semForm(request.POST)
        print("--------", form.errors)
        if form.is_valid():
            try:
                form.save()
                return redirect("/show_sem/")
            except:
                print("--------", sys.exc_info())
        else:
            pass
    else:
        form = semForm()
    return render(request, 'addSemester.html', {'form':form, 'd':d, 'd1':d1})


def adddep(request):
    d = degree.objects.all()
    if request.method == "POST":
        form = depForm(request.POST)
        print("--------", form.errors)
        if form.is_valid():
            try:
                form.save()
                return redirect("/show_dep/")
            except:
                print("--------", sys.exc_info())
        else:
            pass
    else:
        form = depForm()

    return render(request, 'addDepartment.html', {'form':form, 'd':d})


def adddeg(request):
    d= degree.objects.all()
    d1 = department.objects.all()
    if request.method == "POST":
        form = degForm(request.POST)
        print("--------", form.errors)
        if form.is_valid():
            try:
                form.save()
                return redirect("/showdeg/")
            except:
                print("--------", sys.exc_info())
        else:
            pass
    else:
        f = degForm()
    return render(request, 'addDegree.html',{'f':f, 'd':d, 'd1':d1})


def addfac(request):
    d = degree.objects.all()
    d1 = department.objects.all()
    s = subject.objects.all()
    if request.method == "POST":
        form = facForm(request.POST, request.FILES)
        print("--------", form.errors)
        if form.is_valid():
            try:
                handle_uploaded_file(request.FILES['image'])
                form.save()
                return redirect("/show_fac/")
            except:
                print("--------", sys.exc_info())
        else:
            pass
    else:
        form = facForm()
    return render(request, 'addFaculty.html', {'s': s, 'd': d, 'd1': d1, 'form': form})


def addsub(request):
    d = degree.objects.all()
    d1 = department.objects.all()
    s = semester.objects.all()
    if request.method == "POST":
        form = subForm(request.POST, request.FILES)
        print("--------", form.errors)
        if form.is_valid():
            try:
                handle_uploaded_file( request.FILES['img'])
                form.save()
                return redirect("/show_sub/")
            except:
                print("--------", sys.exc_info())
        else:
            pass
    else:
        form = subForm()
    return render(request, 'addSubject.html', {'s': s, 'd': d, 'd1': d1, 'f':form})


def show_deg(request):
    d = degree.objects.all()
    return render(request, 'viewDegree.html', {'d':d})


def show_dep(request):
    d = department.objects.all()
    return render(request, 'viewDepartment.html', {'f':d})


def show_sem(request):
    s = semester.objects.all()
    return render(request, 'viewSemester.html', {'s':s})


def show_sub(request):
    s = subject.objects.all()
    return render(request, 'viewSubject.html', {'s':s})


def show_fac(request):
    s = faculty.objects.all()
    return render(request, 'viewFaculty.html', {'s':s})


def show_stu(request):
    s = student.objects.all()
    return render(request, 'viewStudent.html', {'s':s})


def edit(request, id):
    d = degree.objects.get(id=id)
    return render(request,'editDegree.html', {'d':d})


def update(request, id):
    d = degree.objects.get(id=id)
    form = degForm(request.POST, instance = d)
    if form.is_valid():
        form.save()
        return redirect("/showdeg/")
    return render(request, 'editDegree.html', {'d': d})


def destroy(request, id):
    d = degree.objects.get(id=id)
    d.delete()
    return redirect("/showdeg/")


def dep_edit(request, id):
    d = degree.objects.all()
    f = department.objects.get(id=id)
    return render(request,'editDepartment.html', {'f':f,'d': d})


def dep_update(request, id):
    d = degree.objects.all()
    f = department.objects.get(id=id)
    form = depForm(request.POST, instance=f)
    if form.is_valid():
        form.save()
        return redirect("/show_dep/")
    return render(request, 'editDepartment.html', {'f': f, 'd': d})


def dep_destroy(request, id):
    f = department.objects.get(id=id)
    f.delete()
    return redirect("/show_dep/")


def sem_edit(request, id):
    d = degree.objects.all()
    d1 = department.objects.all()
    s = semester.objects.get(id=id)
    return render(request,'editSemester.html', {'s':s,'d': d, 'd1':d1})


def sem_update(request, id):
    d = degree.objects.all()
    d1 = department.objects.all()
    s = semester.objects.get(id=id)
    form = semForm(request.POST, instance=s)
    if form.is_valid():
        form.save()
        return redirect("/show_sem/")
    return render(request, 'editSemester.html', {'s': s, 'd': d, 'd1':d1})


def sem_destroy(request, id):
    s = semester.objects.get(id=id)
    s.delete()
    return redirect("/show_sem/")


def sub_edit(request, id):
    d = degree.objects.all()
    d1 = department.objects.all()
    f = semester.objects.all()
    s = subject.objects.get(id=id)
    return render(request,'editSubject.html', {'s': s,'d': d, 'd1': d1, 'f': f})


def sub_update(request, id):
    d = degree.objects.all()
    d1 = department.objects.all()
    f = semester.objects.all()
    s = subject.objects.get(id=id)
    form = subForm(request.POST, instance=s)
    print('----',form)
    if form.is_valid():
        form.save()
        print('--', form)
        return redirect("/show_sub/")
    return render(request, 'editSubject.html', {'s': s, 'd': d, 'd1': d1, 'f': f})


def sub_destroy(request, id):
    s = subject.objects.get(id=id)
    s.delete()
    return redirect("/show_sub/")


def fac_edit(request, id):
    d = degree.objects.all()
    d1 = department.objects.all()
    f = subject.objects.all()
    s = faculty.objects.get(id=id)
    form = faForm()
    return render(request,'editFaculty.html', {'s': s,'d': d, 'd1': d1, 'f': f, 'form':form})


def fac_update(request, id):
    d = degree.objects.all()
    d1 = department.objects.all()
    f = subject.objects.all()
    s = faculty.objects.get(id=id)
    form = faForm(request.POST, instance=s)
    print('----',form)
    if form.is_valid():
        print(form.errors)

        form.save()
        print('--', form)
        return redirect("/show_fac/")
    return render(request, 'editFaculty.html', {'s': s, 'd': d, 'd1': d1, 'f': f, 'form':form})


def fac_destroy(request, id):
    s = faculty.objects.get(id=id)
    s.delete()
    return redirect("/show_fac/")


def stu_edit(request, id):
    d = degree.objects.all()
    d1 = department.objects.all()
    f = semester.objects.all()
    s = student.objects.get(id=id)
    form = stForm()
    return render(request,'editStudent.html', {'s': s,'d': d, 'd1': d1, 'f': f, 'form':form})


def stu_update(request, id):
    d = degree.objects.all()
    d1 = department.objects.all()
    f = semester.objects.all()
    s = student.objects.get(id=id)
    form = stForm(request.POST, instance=s)
    print('----',form)
    if form.is_valid():
        print(form.errors)

        form.save()
        print('--', form)
        return redirect("/show_stu/")
    return render(request, 'editStudent.html', {'s': s, 'd': d, 'd1': d1, 'f': f, 'form':form})


def stu_destroy(request, id):
    s = student.objects.get(id=id)
    s.delete()
    return redirect("/show_stu/")


def admin_login(request):
    if request.method == "POST":
        e = request.POST.get("username")
        p = request.POST.get("password")
        val = user.objects.filter(username=e,password=p,is_admin=1).count()
        print('---', val)
        if val == 1:
            data = user.objects.filter(username=e,password=p)
            print("++++++++", data)
            for items in data:
                request.session['username'] = items.username
                request.session['id'] = items.id
                return redirect('/index/')
        else:
            messages.error(request, "Invalid username and password")
            return render(request, "login.html")
    else:
        pass
    return render(request, "login.html")


def logout(request):
    try:
        del request.session['id']
    except:
        return redirect('/login/')
    return redirect('/login/')