import cloudinary.uploader
from django.shortcuts import get_object_or_404
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework import views as rest_basic_views
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import SAFE_METHODS, BasePermission, IsAuthenticated
from rest_framework.response import Response

from crm_for_companies.api_companies.models import Company, UserModel
from crm_for_companies.api_companies.serializers import (
    CompanyCreateSerializer,
    CompanySerializer,
    CompanySerializerWithEmployees,
)


def get_first_user_pk():
    user = UserModel.objects.all().first()

    if user is not None:
        return user.pk
    else:
        return None


class IsCompanyOwner(BasePermission):
    message = "Only Owner can see company details."

    def has_permission(self, request, view):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False
        # Allow access for superusers
        if request.user.is_superuser:
            return True
        if request.method:
            return True

        return False

    def has_object_permission(self, request, view, obj):
        print("in_has_object_permission")
        # Allow access for superusers
        if request.user.is_superuser:
            return True
        return request.user in UserModel.objects.filter(
            company__owner=request.user, company__pk=obj["id"].value
        )


company_request_body_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "owner": openapi.Schema(
            type=openapi.TYPE_ARRAY,
            items=openapi.Items(type=openapi.TYPE_INTEGER),
        ),
        "name": openapi.Schema(type=openapi.TYPE_STRING),
        "description": openapi.Schema(type=openapi.TYPE_STRING),
        "logo": openapi.Schema(type=openapi.TYPE_STRING),
    },
    required=["owner", "name", "description", "logo"],
    example={
        "name": "Example Company",
        "description": "Some example company description",
        "logo": "/home/yd/Screenshot-10.png",
        "owner": [
            get_first_user_pk(),
        ],
    },
)


class CompanyListApiView(rest_basic_views.APIView):
    """
    Get list of all companies data.

    This returns list of all companies from DB. Needs  authentication token. No other parameters.

    """

    queryset = Company.objects.all()
    serializer_class = CompanySerializerWithEmployees
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        serializer = self.serializer_class(self.get_queryset(), many=True)

        return Response(
            {"data": serializer.data, "status": status.HTTP_200_OK},
            status=status.HTTP_200_OK,
        )

    def get_queryset(self):
        company_id = self.request.query_params.get("company_id")
        queryset = self.queryset.all()
        if company_id:
            queryset = queryset.filter(id=company_id)
        return queryset


class CreateCompanyApiView(rest_basic_views.APIView):
    """
    Create new company.

    Save new company in the database.

    """

    queryset = Company.objects.all()

    # @swagger_auto_schema(
    #     request_body=openapi.Schema(
    #         type=openapi.TYPE_OBJECT,
    #         properties={
    #             'owner': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_INTEGER)),
    #             'name': openapi.Schema(type=openapi.TYPE_STRING),
    #             'description': openapi.Schema(type=openapi.TYPE_STRING),
    #             'logo': openapi.Schema(type=openapi.TYPE_STRING),
    #         },
    #         required=['owner', 'name', 'description', 'logo'],
    #     )
    # )
    @swagger_auto_schema(
        request_body=company_request_body_schema,
        responses={200: CompanyCreateSerializer},
    )
    def post(self, request, *args, **kwargs):
        serializer = CompanyCreateSerializer(
            data=request.data, context={"request": request}
        )
        if serializer.is_valid(raise_exception=True):
            file = request.data.get("logo")
            logo = cloudinary.uploader.upload(file)
            serializer.validated_data["logo"] = logo["url"]
            serializer.save()
            return Response(
                {
                    "data": serializer.data,
                    "errors": serializer.errors,
                    "status": status.HTTP_201_CREATED,
                },
                status=status.HTTP_201_CREATED,
            )

        return Response(
            {"errors": serializer.errors, "status": status.HTTP_400_BAD_REQUEST}
        )


class DetailsCompanyApiView(rest_basic_views.APIView):
    http_method_names = ["get", "delete", "put"]
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    permission_classes = (IsCompanyOwner,)

    def get(self, request, pk):
        """
        Get company specific data

        Retrieve company data when PK is specified in URL
        """
        instance = self.serializer_class(get_object_or_404(Company, pk=pk))
        self.check_object_permissions(self.request, instance)

        return Response(instance.data)

    @swagger_auto_schema(request_body=company_request_body_schema)
    def put(self, request, pk):
        """
        Edit (overwrite) company data.

        Edit data for company identified by PK
        """
        instance = get_object_or_404(Company, pk=pk)

        serializer = self.serializer_class(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "data": serializer.data,
                    "errors": serializer.errors,
                    "status": status.HTTP_200_OK,
                },
                status=status.HTTP_200_OK,
            )

        return Response(
            {"errors": serializer.errors, "status": status.HTTP_400_BAD_REQUEST},
            status=status.HTTP_400_BAD_REQUEST,
        )

    def delete(self, request, pk):
        """
        Delete company from DB.

        Deletes data for company identified by PK.
        """
        try:
            instance = Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            return Response(
                {"status": status.HTTP_404_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND
            )
        instance.delete()
        return Response(
            {"status": status.HTTP_204_NO_CONTENT}, status=status.HTTP_204_NO_CONTENT
        )
