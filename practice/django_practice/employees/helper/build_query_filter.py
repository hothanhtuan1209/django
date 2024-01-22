from django.db.models import Q


def build_query_filter(request_data):
    """
    Helper function to build the query filter based on name, department
    or any field.
    """

    name = request_data.get('name', None)
    department_names = request_data.getlist('department', None)
    query_filter = Q()

    if name:
        query_filter |= Q(first_name__icontains=name) | Q(last_name__icontains=name)

    if department_names:
        for department in department_names:
            query_filter |= Q(department__name=department)

    return query_filter
