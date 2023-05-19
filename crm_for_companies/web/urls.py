from django.urls import path

from crm_for_companies.web.views import UserDetailsView, EditUserView

urlpatterns = (
    path('details/<int:pk>/', UserDetailsView.as_view(), name='Details'),
    path('edit/<int:pk>/', EditUserView.as_view(), name='Edit'),
)
