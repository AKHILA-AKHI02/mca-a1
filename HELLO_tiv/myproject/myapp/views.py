from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse 
from .models import EmployeeModel  
from .forms import EmployeeForm
from .models import FacultyModel 
from .forms import FacultyForm

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
def delete_employee(request,pk):
    EmployeeModel.objects.get(id=pk) .delete()
    return render(request,
                  'delete_employee.html')
def update_employee(request,pk):
    obe = get_object_or_404(EmployeeModel, id=pk)
    if request.method == 'POST':
        obf = EmployeeForm(request.POST, instance=obe)
        if obf.is_valid():
            obf.save()
        return redirect('view_employee')#, id=pk
    else:
        formdata=EmployeeForm(instance=obe)
    return render(request, "update_employee.html", {'form':formdata})
def insert_faculty(request):
    context ={}# dictionary for initial data with field names as keys
    ob_form = FacultyForm(request.POST or None)
    if ob_form.is_valid():
        ob_form.save()
        return HttpResponse("Data Saved")
    context['form']= ob_form
    return render(request, "insert_faculty.html", context)  
#view employee data
def view_faculty(request):
    ob=FacultyModel.objects.all().values()
    context={
        'data':ob
        }
    temp=loader.get_template('view_faculty.html')
    return HttpResponse(temp.render(context,request))
def delete_faculty(request,pk):
    FacultyModel.objects.get(id=pk) .delete()
    return render(request,
                  'delete_faculty.html')
def update_faculty(request,pk):
    obe = get_object_or_404(FacultyModel, id=pk)
    if request.method == 'POST':
        obf = FacultyForm(request.POST, instance=obe)
        if obf.is_valid():
            obf.save()
        return redirect('view_faculty')#, id=pk
    else:
        formdata=FacultyForm(instance=obe)
    return render(request, "update_faculty.html", {'form':formdata})