from django.shortcuts import render,redirect
from .forms import *
from subject.models import Subjects
from django.contrib.auth.decorators import login_required
from department.models import *
from django.db.models import Q

# Create your views here.

@login_required(login_url='/login')
def add_subject(request):
    a = Departments.objects.all()
    b = Semesters.objects.all()
    if(request.method == 'POST'):
        try:
            Subjects.objects.get(department = Departments.objects.get(id=request.POST['department']),name=request.POST['name'])
            return render(request,'subject_add.html',{'d':True})
        except Subjects.DoesNotExist:
            Subjects.objects.create(    
                name =request.POST['name'],
                description = request.POST['description'],
                department = Departments.objects.get(id=request.POST['department']),
                semester = Semesters.objects.get(id=request.POST['semester'])
            )
        return redirect('/subject_view')
    else:
        return render(request,'subject_add.html',{'a':a,'b':b}) 

@login_required(login_url='/login')
def view_subject(request):
    a = Subjects.objects.all()
    b = Subjects.objects.filter(department=request.user.department)
    search = request.GET.get('search','')
    if search:
        a=a.filter(Q(name__icontains=search)|Q(department__departmentname__icontains=search))
        b=b.filter(Q(name__icontains=search))
    return render(request,'subject_view.html',{'a':a,'b':b})
    
@login_required(login_url='/login')
def delete_subject(request,id):
    data = Subjects.objects.get(id=id)
    data.delete()
    return redirect('/subject_view')

@login_required(login_url='/login')
def edit_subject(request,id):
    a = Subjects.objects.get(id=id)
    b = Departments.objects.all()
    c = Semesters.objects.all()
    if request.method == 'POST':
            a.name = request.POST['name']
            a.description = request.POST['description']
            a.department = Departments.objects.get(id=request.POST['department'])
            a.semester = Semesters.objects.get(id=request.POST['semester'])
            a.save()
            return redirect('/subject_view')
    return render(request,'subject_edit.html',{'a':a,'b':b,'c':c})

