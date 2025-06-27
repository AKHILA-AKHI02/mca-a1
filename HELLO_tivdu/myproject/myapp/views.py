from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse 
from .models import EmployeeModel  
from .forms import EmployeeForm
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
from django.shortcuts import get_object_or_404, redirect
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
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = HttpResponse(content_type='application/pdf')
    pisa_status = pisa.CreatePDF(html, dest=result)
    return result if not pisa_status.err else HttpResponse('PDF generation failed')

def pdf_view(request):
    data = {
        'name': 'Praveen Choudhary',
        'course': 'Django Development',
        'date': '2025-06-27'
    }
    return render_to_pdf('pdf_template.html', data)    