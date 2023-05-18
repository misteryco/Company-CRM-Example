from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from crm_for_companies.api_employees.views import EmployeeListApiView, EmployeeCreateApiView, EmployeeUpdateApiView, \
    EmployeeDeleteApiView, EmployeeDetailsApiView, GetUserByToken, RegisterView, LogOutUser

urlpatterns = (
    path('', EmployeeListApiView.as_view(), name='api list employee'),
    path('create/', EmployeeCreateApiView.as_view(), name='api create employee'),
    path('details/<int:pk>', EmployeeDetailsApiView.as_view(), name='api details employee'),
    path('update/<int:pk>', EmployeeUpdateApiView.as_view(), name='api update employee'),
    path('delete/<int:pk>', EmployeeDeleteApiView.as_view(), name='api delete employee'),
    path('get-user-token/', GetUserByToken.as_view(), name='example view'),
    path('obtain-auth-token/', obtain_auth_token, name='api_token_auth'),
    path('register-user-by-id/', RegisterView.as_view(), name='api_token_auth'),
    path('log-out-user/', LogOutUser.as_view(), name='log_out_user'),
)
