from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    """
    This is form to create a new employee.
    """

    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'birthday', 'email', 'gender', 'status', 'department']
