from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Employee
from django_practice.settings import PAGE_SIZE
from .helper.build_query_filter import build_query_filter


def employees(request):
    """
    This function gets a list of employees from the database.
    """

    request_data = request.GET
    query_filter = build_query_filter(request_data)

    order_by = request.GET.get("order_by", "-created_at")
    employees_queryset = Employee.objects.filter(query_filter).order_by(order_by).values(
        'id', 'first_name', 'last_name', 'birthday', 'department__name'
    )

    paginator = Paginator(employees_queryset, PAGE_SIZE)
    page = request.GET.get("page", 1)

    try:
        employees_page = paginator.page(page)
    except (PageNotAnInteger, EmptyPage):
        employees_page = paginator.page(1)

    context = {
        "employees": list(employees_page),
    }

    return render(request, "list.html", context)
