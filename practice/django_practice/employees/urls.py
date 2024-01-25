from django.urls import path
from .views import employee_detail, employees

urlpatterns = [
    path('', employees, name='employees'),
    path('dt/<str:employee_id>/', employee_detail, name='employee_detail'),
]
