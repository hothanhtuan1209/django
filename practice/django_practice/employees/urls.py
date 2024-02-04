from django.urls import path
from .views import employee_detail, employees, new_employee, update_employee, delete_employee

urlpatterns = [
    path('', employees, name='employees'),
    path('detail/<str:employee_id>/', employee_detail, name='employee_detail'),
    path('create/', new_employee, name='create_employee'),
    path('update/<str:employee_id>/', update_employee, name='employee_update'),
    path('delete/<str:employee_id>/', delete_employee, name='delete_employee')
]
