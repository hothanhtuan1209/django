from django import forms
from .models import Employee
from .validate.validations import validate_name, validate_age


class EmployeeForm(forms.ModelForm):
    """
    This is form to create a new employee.
    """
    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        validate_name(first_name)
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        validate_name(last_name)
        return last_name

    def clean_birthday(self):
        birthday = self.cleaned_data['birthday']
        validate_age(birthday)
        return birthday

    class Meta:
        model = Employee
        fields = '__all__'
