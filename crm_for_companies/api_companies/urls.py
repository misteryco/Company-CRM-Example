from django.urls import path

from crm_for_companies.api_companies.views import CompanyListApiView, CustomCompanyListApiView, \
    CustomCreateCompanyApiView, DetailsCompanyApiView

urlpatterns = (
    path('generic/', CompanyListApiView.as_view(), name='api generic list company'),
    path('', CustomCompanyListApiView.as_view(), name='api list company'),
    path('create/', CustomCreateCompanyApiView.as_view(), name='api create company'),
    path('delete/<int:pk>/', DetailsCompanyApiView.as_view(), name='api details company'),
)
