from django.shortcuts import render,HttpResponse
from . models import Department,Role,Employee
from datetime import datetime
def index(request):
    return render(request, 'index.html')
# Create your views here.
def all_emp(request):
    emps=Employee.objects.all()
    context={
        'emps':emps
    }
    print(context)
    return render(request, 'all_emp.html',context)

def add_emp(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name = request.POST['last_name']
        dept = request.POST['dept']
        salary = int(request.POST['salary'])
        bonus= int(request.POST['bonus'])
        role = int(request.POST['role'])
        phone =int(request.POST['phone'])
        new_emp=Employee(first_name=first_name,last_name=last_name,dept_id=dept,salary=salary,bonus=bonus,role_id=role,phone=phone,hire_date=datetime.now())
        new_emp.save()
        return HttpResponse("Employee details added sucessfully")
    elif request.method=="GET":
          return render(request, 'add_emp.html')
    else:
        return HttpResponse("something wrong")

def remove_emp(request,emp_id=0):
    if emp_id:
        try:
            emp_to_be_remove=Employee.objects.get(id=emp_id)
            emp_to_be_remove.delete()
            return HttpResponse("sucessfully Deleted")
        except:
            return HttpResponse("something error")
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    print(context)
    return render(request, 'remove_emp.html',context)

def filter_emp(request):
    return render(request, 'filter_emp.html')