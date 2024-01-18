from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

from .models import Employee


def employees(request):
    """
    This function gets a list of employees from the database.
    """

    employees_queryset = Employee.objects.all()

    # Filter by name
    employees_name = request.GET.get('name')
    if employees_name:
        employees_queryset = employees_queryset.filter(
            Q(first_name__icontains=employees_name)
            | Q(last_name__icontains=employees_name)
        )

    # Filter by department
    department_name = request.GET.get('department')
    if department_name:
        employees_queryset = employees_queryset.filter(
            department__name=department_name
        )

    items_in_page = 20
    paginator = Paginator(employees_queryset, items_in_page)
    page = request.GET.get('page', 1)

    try:
        employees_page = paginator.page(page)
    except PageNotAnInteger:
        employees_page = paginator.page(1)
    except EmptyPage:
        employees_page = paginator.page(paginator.num_pages)

    context = [
        {
            'id': employee.id,
            'full_name': employee.get_full_name(),
            'department': employee.department.name
        }
        for employee in employees_page
    ]

    return render(request, 'list.html', context)
