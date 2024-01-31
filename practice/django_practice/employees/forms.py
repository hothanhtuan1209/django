from django import forms
from .models import Employee
from .validate.validations import validate_name


class EmployeeForm(forms.ModelForm):
    """
    This is form to create a new employee.
    """

    first_name = forms.CharField(validators=[validate_name])
    last_name = forms.CharField(validators=[validate_name])

    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'birthday', 'email', 'gender', 'status', 'department']
