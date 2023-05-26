from django.urls import path

from crm_for_companies.web.views import UserDetailsView, HomePage, EditUserView

urlpatterns = (
    path('', HomePage.as_view(), name='Home page'),
    path('details/<int:pk>/', UserDetailsView.as_view(), name='Details'),
    # path('edit/<int:pk>/', edit_user_view, name='Edit'),  # protected with decorator
    # path('edit-cookie-protected/<int:pk>/', edit_user_cookie_protection_view, name='Edit Cookie'),
    # protected with cookie
    path('edit-no-csrft/<int:pk>/', EditUserView.as_view(), name='Edit username and email form'),
)
