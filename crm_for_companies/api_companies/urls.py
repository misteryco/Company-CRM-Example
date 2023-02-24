from django.urls import path

from crm_for_companies.api_companies.views import CompanyListApiView, CreateCompanyApiView, DetailsCompanyApiView

urlpatterns = (
    path('', CompanyListApiView.as_view(), name='api list company'),
    path('create/', CreateCompanyApiView.as_view(), name='api create company'),
    path('details/<int:pk>/', DetailsCompanyApiView.as_view(), name='api details company'),
)
