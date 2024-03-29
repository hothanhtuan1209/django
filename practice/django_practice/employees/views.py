from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt

from .models import Employee
from django_practice.settings import PAGE_SIZE
from .helper.build_query_filter import build_query_filter
from .forms import EmployeeForm


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


@require_http_methods(["GET"])
def employee_detail(request, employee_id):
    """
    This function to get detail employee.
    """

    employee = get_object_or_404(Employee, id=employee_id)
    context = {'employee': employee}
    return render(request, 'detail.html', context)


@csrf_exempt
@require_http_methods(["GET", "POST", "PUT", "PATCH"])
def update_employee(request, employee_id):
    """
    This function to update information of employee.
    """

    employee = get_object_or_404(Employee, id=employee_id)

    form = EmployeeForm(request.POST or None, instance=employee)

    if form.is_valid():
        employee = form.save()
        detail_url = reverse('employee_detail', args=[str(employee.id)])
        return redirect(detail_url)

    return render(request, 'employee_update.html', {'form': form, 'employee': employee})


@csrf_exempt
@require_http_methods(['GET', 'POST'])
def new_employee(request):
    """
    This is function to create a new employee.
    """

    if request.method == 'POST':
        form = EmployeeForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('employees')

    else:
        form = EmployeeForm()

    context = {'form': form}
    return render(request, 'new_employee.html', context)
