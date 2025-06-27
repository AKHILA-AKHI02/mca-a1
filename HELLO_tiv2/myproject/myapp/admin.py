from django.contrib import admin
from .models import EmployeeModel  
from .models import StudentsModel

admin.site.register(EmployeeModel)
admin.site.register(StudentsModel)

# Register your models here.
