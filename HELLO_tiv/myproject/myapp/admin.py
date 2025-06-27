from django.contrib import admin
from .models import EmployeeModel
from .models import FacultyModel
admin.site.register(EmployeeModel)
admin.site.register(FacultyModel)

# Register your models here.
