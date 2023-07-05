from django.contrib import admin
from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="CRM for Companies API from DOCKER",
        default_version="v.0.0.1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="SomeOne@codeit.pro"),
        license=openapi.License(name="Some License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    # enable browsable API
    path("api-accounts/", include("rest_framework.urls")),
    # urls for apps
    path("api_companies/", include("crm_for_companies.api_companies.urls")),
    path("api_employees/", include("crm_for_companies.api_employees.urls")),
    # urls for gui
    path("web/", include("crm_for_companies.web.urls")),
    # urls for swagger
    # acceptable <format> in next line are .json and .yaml
    path(
        "swagger<format>/", schema_view.without_ui(cache_timeout=0), name="schema-json"
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
