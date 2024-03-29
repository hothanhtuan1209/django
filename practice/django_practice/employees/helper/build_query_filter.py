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
        query_filter &= Q(first_name__icontains=name) | Q(last_name__icontains=name)

    if departments:
        query_filter &= Q(department__id__in=departments)

    return query_filter
