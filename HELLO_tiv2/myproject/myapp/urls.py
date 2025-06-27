from django.urls import path
from . import views
urlpatterns = [
   path('insert_employee/',views.insert_employee, name='insert_employee'),
   path('view_employee/', views.view_employee,  name = 'view_employee'),
   path('insert_students/',views.insert_students, name='insert_students'),
   path('view_students/', views.view_students,  name = 'view_students'),
   
# other paths as needed
]
