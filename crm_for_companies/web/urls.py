from django.urls import path

from crm_for_companies.web.views import UserDetailsView, edit_user_view, HomePage, EditUserNoCSRFTView

urlpatterns = (
    path('', HomePage.as_view(), name='Home page'),
    path('details/<int:pk>/', UserDetailsView.as_view(), name='Details'),
    path('edit/<int:pk>/', edit_user_view, name='Edit'),
    path('edit-no-csrft/<int:pk>/', EditUserNoCSRFTView.as_view(), name='Edit No CSRFT'),
)
