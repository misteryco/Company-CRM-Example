from django.urls import path

from crm_for_companies.api_employees.views import EmployeeListApiView, EmployeeCreateApiView, EmployeeUpdateApiView, \
    EmployeeDeleteApiView, EmployeeDetailsApiView

urlpatterns = (
    path('', EmployeeListApiView.as_view(), name='api list employee'),
    path('create/', EmployeeCreateApiView.as_view(), name='api create employee'),
    path('details/<int:pk>', EmployeeDetailsApiView.as_view(), name='api details employee'),
    path('update/<int:pk>', EmployeeUpdateApiView.as_view(), name='api update employee'),
    path('delete/<int:pk>', EmployeeDeleteApiView.as_view(), name='api delete employee'),
)
