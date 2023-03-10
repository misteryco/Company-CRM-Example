from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # enable browsable API
    path('api-auth/', include('rest_framework.urls')),

    # urls for apps
    path('api_companies/', include('crm_for_companies.api_companies.urls')),
    path('api_employees/', include('crm_for_companies.api_employees.urls')),

]
