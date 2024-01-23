from django.urls import path
from .views import employees, EmployeeDetailView

urlpatterns = [
    path('', employees, name='emloyees'),
    path('<uuid:employee_id>', EmployeeDetailView.as_view(), name='employee_detail')
]
