from django.urls import path
from . import views
urlpatterns = [
   path('insert_employee/',views.insert_employee, name='insert_employee'),
   path('view_employee/', views.view_employee,  name = 'view_employee'),
   path('insert_faculty/', views.insert_faculty, name='insert_faculty'),
   path('view_faculty/', views.view_faculty, name='view_faculty'),
   path('delete_employee/<int:pk>',
        views.delete_employee,
        name = 'delete_employee'),
   path('update_employee/<int:pk>', views.update_employee,
         name = 'update_employee'),       

   path('delete_faculty/<int:pk>',
        views.delete_faculty,
        name = 'delete_faculty'),
     
   path('update_faculty/<int:pk>', views.update_faculty,
           name = 'update_faculty'),     
# other paths as needed
]         
# other paths as needed

# other paths as needed

