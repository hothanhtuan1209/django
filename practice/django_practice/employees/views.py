from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

from .models import Employee
from django_practice.settings import PAGE_SIZE


def build_query_filter(name, department):
    """
    Helper function to build the query filter based on name and department.
    """
    query_filter = Q()

    if name:
        query_filter |= Q(first_name__icontains=name) | Q(last_name__icontains=name)

    if department:
        query_filter &= Q(department__name=department)

    return query_filter


def employees(request):
    """
    This function gets a list of employees from the database.
    """

    employees_name = request.GET.get("name")
    department_name = request.GET.get("department")
    order_by = request.GET.get("order_by", "-created_at")

    query_filter = build_query_filter(employees_name, department_name)
    employees_queryset = Employee.objects.filter(query_filter).order_by(order_by)

    paginator = Paginator(employees_queryset, PAGE_SIZE)
    page = request.GET.get("page", 1)

    try:
        employees_page = paginator.page(page)
    except PageNotAnInteger:
        employees_page = paginator.page(1)
    except EmptyPage:
        employees_page = paginator.page(paginator.num_pages)

    context = {
        "employees": [
            {
                "id": employee.id,
                "full_name": employee.get_full_name(),
                "department": employee.department.name,
            }
            for employee in employees_page
        ]
    }

    return render(request, "list.html", context)
