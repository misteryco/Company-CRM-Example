from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from crm_for_companies.api_employees.views import (
    CustomAuthToken,
    GetUserByToken,
    LogOutUser,
    RegisterView,
)

urlpatterns = (
    path("get-user-token/", GetUserByToken.as_view(), name="get user by token"),
    # path('obtain-auth-token/', obtain_auth_token, name='api_token_auth'),
    path("obtain-auth-token/", CustomAuthToken.as_view(), name="api_token_auth"),
    path("register-user-by-id/", RegisterView.as_view(), name="register_user"),
    path("log-out-user/", LogOutUser.as_view(), name="log_out_user"),
)

# from django.urls import path
#
# from crm_for_companies.web.views import UserDetailsView, HomePage, EditUserView
#
# urlpatterns = (
#
#
#
#
#     # path('', HomePage.as_view(), name='Home page'),
#     # path('details/<int:pk>/', UserDetailsView.as_view(), name='Details'),
#     # # path('edit/<int:pk>/', edit_user_view, name='Edit'),  # protected with decorator
#     # # path('edit-cookie-protected/<int:pk>/', edit_user_cookie_protection_view, name='Edit Cookie'),
#     # # protected with cookie
#     # path('edit-no-csrft/<int:pk>/', EditUserView.as_view(), name='Edit'),
# )
