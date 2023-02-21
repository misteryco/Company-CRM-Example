from django.urls import path

from crm_for_companies.api_employees.views import EmployeeListApiView

urlpatterns = (
    path('', EmployeeListApiView.as_view(), name='api list employee'),
)
