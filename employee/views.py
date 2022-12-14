from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee, Department, Roles 
from datetime import datetime
from django.db.models import Q


# Create your views here.

def hello_world(request):
    return render (request,'hello.html', { 'name':'aditya Khanna'})

def about_page(request):
    return render (request,'about.html')

def home_page(request):
    return render (request,'index.html')

def all_employee(request):
    # Model.object.all() to 
    emp = Employee.objects.all()
    context = {'emp':emp}
    print(context)
    return render (request,'all-employee.html', context)

def add_employee(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dept = request.POST['dept']
        role = request.POST['role']
        phone = int(request.POST['phone'])
        age = int(request.POST['age'])
        bonus = int(request.POST['bonus'])
        salary = int(request.POST['salary'])
        bio = request.POST['bio']
        
        new_emp= Employee(first_name = first_name, last_name = last_name, role_id = role, salary=salary, dept_id = dept, bonus = bonus, age = age, phone = phone, bio = bio, hire_date=datetime.now())
        new_emp.save()
        return HttpResponse("Employee Added Successfully")  


    elif request.method =='GET':
        dep = Department.objects.all()
        context = {'dep':dep}
        return render (request,'add-employee.html', context)
    else:
        return HttpResponse("Error")

def remove_employee(request):
    return HttpResponse("Employee Added Successfully")  

def filter_employee(request):
    if request.method=='POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']

        emp = Employee.objects.all()
        if name:
            emp = emp.filter (Q(first_name__icontains = name) | Q(last_name__icontains = name))

        if dept:
            emp = emp.filter(Q(dept__department_name__icontains = dept))
        
        if role:
            emp = emp.filter(role__role_name = role)

        context = {
            'emp' : emp
        }
        return render (request, 'all-employee.html', context)
        
    elif request.method =='GET':
            return render (request,'filter-employee.html')
    else:
        return HttpResponse("eror")