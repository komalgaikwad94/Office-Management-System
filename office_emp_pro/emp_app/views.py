from django.shortcuts import render,HttpResponse
from .models import Department,Employee,Role
from datetime import datetime
from django.db.models import Q


# Create your views here.
def indexview(request):
    return render(request,'index.html')

def all_emp(request):
    emps=Employee.objects.all()
    print(emps)
    context={
        'emps':emps
    }
    print(context)
    return render(request,'view_all_emp.html',context)

def add_emp(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name = request.POST['last_name']
        dept = request.POST['dept']
        salary = int(request.POST['salary'])
        bonus=int(request.POST['bonus'])
        role=request.POST['role']
        phone = int(request.POST['phone'])
        
        new_emp=Employee(first_name=first_name,last_name=last_name,salary=salary,bonus=bonus,dept_id=dept,role_id=role,hire_date=datetime.now(),phone=phone)
        new_emp.save()
        return HttpResponse('Employee Added Successfully')

    elif request.method=='GET':
        return  render(request,'add_emp.html')

    else:
        return  HttpResponse('An Exception Occured! Employee has not been added')


def remove_emp(request,emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed=Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse('Employee removed successfully')
        except:
            return  HttpResponse("Please Enter a valid EMP ID")
    emps=Employee.objects.all()
    context={
        'emps':emps
    }
    return render(request,'remove_emp.html',context)

def filter_emp(request):
    if request.method=='POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps=Employee.objects.all()
        if name:
            emps=emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains=name) )
        if dept:
            emps=emps.filter(dept__name =dept)
        if role:
            emps=emps.filter(role__name=role)
            
        context={
            'emps':emps
        }
        return  render(request,'view_all_emp.html',context)
    
    elif request.method=='GET':
        return render(request,'filter_emp.html')
    else:
        return HttpResponse('Error Occured')
