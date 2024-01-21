from django.db.models import Q


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
