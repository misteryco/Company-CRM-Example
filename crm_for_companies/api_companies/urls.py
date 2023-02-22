from django.urls import path

from crm_for_companies.api_companies.views import CompanyListApiView, CustomCompanyListApiView, \
    CustomCreateCompanyApiView, CustomDeleteCompanyApiView

urlpatterns = (
    path('', CompanyListApiView.as_view(), name='api list company'),
    path('custom/', CustomCompanyListApiView.as_view(), name='api custom list company'),
    path('custom/create/', CustomCreateCompanyApiView.as_view(), name='api custom create company'),
    path('custom/delete/<int:pk>/', CustomDeleteCompanyApiView.as_view(), name='api custom delete company'),
)
