from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Employee


def employees(request, page):
    """
    This function gets a list of employees from the database.
    """

    if request.method == "GET":
        employees = Employee.objects.all()
        items_in_page = 20
        paginator = Paginator(employees, items_in_page)

        try:
            employees_page = paginator.page(page)
        except PageNotAnInteger:
            employees_page = paginator.page(1)
        except EmptyPage:
            employees_page = paginator.page(paginator.num_pages)

        employees_data = [
            {
                'id': employee.id,
                'full_name': employee.get_full_name(),
                'department': employee.department.name
            }
            for employee in employees_page
        ]

        return JsonResponse({'employees': employees_data})
