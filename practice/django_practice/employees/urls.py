from django.urls import path
from .views import employees

urlpatterns = [
    path('list/<int:page>', employees, name='emloyees')
]
