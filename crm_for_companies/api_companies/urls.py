from django.urls import path

from crm_for_companies.api_companies.views import CompanyListApiView

urlpatterns = (
    path('', CompanyListApiView.as_view(), name='api list company'),
)
