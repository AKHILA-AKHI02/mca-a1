from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse 
from .models import EmployeeModel  
from .forms import EmployeeForm
from .models import StudentsModel  
from .forms import StudentsForm
#display form & save data  typed in form 
def insert_employee(request):
    context ={}# dictionary for initial data with field names as keys
    ob_form = EmployeeForm(request.POST or None)
    if ob_form.is_valid():
        ob_form.save()
        return HttpResponse("Data Saved")
    context['form']= ob_form
    return render(request, "insert_employee.html", context)  
#view employee data
def view_employee(request):
    ob=EmployeeModel.objects.all().values()
    context={
        'data':ob
        }
    temp=loader.get_template('view_employee.html')
    return HttpResponse(temp.render(context,request))
def insert_students(request):
    context ={}# dictionary for initial data with field names as keys
    ob_form = StudentsForm(request.POST or None)
    if ob_form.is_valid():
        ob_form.save()
        return HttpResponse("Data Saved")
    context['form']= ob_form
    return render(request, "insert_students.html", context)  
#view students data
def view_students(request):
    ob=StudentsModel.objects.all().values()
    context={
        'data':ob
        }
    temp=loader.get_template('view_students.html')
    return HttpResponse(temp.render(context,request))