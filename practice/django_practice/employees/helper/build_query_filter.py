from django.db.models import Q


def build_query_filter(request_data):
    """
    Helper function to build the query filter based on name, department
    or any field.
    """

    name = request_data.get('name', None)
    departments = request_data.getlist('departments', None)
    query_filter = Q()

    if name:
        query_filter |= Q(first_name__icontains=name) | Q(last_name__icontains=name)

    if departments:
        department_query = Q()
        for department_id in departments:
            department_query |= Q(department__id=department_id)

        query_filter &= department_query

    return query_filter
