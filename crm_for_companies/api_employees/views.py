import cloudinary.uploader
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics as generic_rest_views
from rest_framework import status
from rest_framework import views as rest_basic_views
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from crm_for_companies.api_companies.models import Company
from crm_for_companies.api_employees.models import Employee
from crm_for_companies.api_employees.serializers import (
    CreateEmployeeSerializer,
    EmployeeSerializerWithCompany,
    RegisterSerializer,
)
from crm_for_companies.api_employees.tasks import send_welcome_email_to_new_users
from crm_for_companies.core.employees_functions import employee_request_body


class EmployeeListApiView(rest_basic_views.APIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializerWithCompany
    # to check authentication
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(
        operation_summary="Retrieve all Employees from DB.",
        operation_description="This endpoint shows all Employees.",
        responses={200: serializer_class},
    )
    def get(self, request):
        serializer = self.serializer_class(self.get_queryset(), many=True)

        return Response(
            {"data": serializer.data, "status": status.HTTP_200_OK},
            status=status.HTTP_200_OK,
        )

    def get_queryset(self):
        company_id = self.request.query_params.get("company_id")
        queryset = self.queryset

        if company_id:
            queryset = queryset.filter(company_id=company_id)

        return queryset.all()


class EmployeeCreateApiView(rest_basic_views.APIView):
    queryset = Employee.objects.all()
    serializer_class = CreateEmployeeSerializer

    # Other method to define swagger schema
    @swagger_auto_schema(
        request_body=employee_request_body,
        responses={201: serializer_class},
    )
    def post(self, request, *args, **kwargs):
        """
        Record new Employee in DB.

        This endpoint create a new Employee for specific company.
        """
        try:
            Company.objects.get(pk=request.data["company"])
        except Company.DoesNotExist:
            return Response(
                {
                    "errors": f"Company with id:{request.data['company']} does not exist.",
                    "status": status.HTTP_400_BAD_REQUEST,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )

        if serializer.is_valid(raise_exception=True):
            file = request.data.get("photo")
            photo = cloudinary.uploader.upload(file)
            serializer.validated_data["photo"] = photo["url"]
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
            {"errors": serializer.errors, "status": status.HTTP_400_BAD_REQUEST},
            status=status.HTTP_400_BAD_REQUEST,
        )


class EmployeeUpdateApiView(generic_rest_views.UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = CreateEmployeeSerializer

    @swagger_auto_schema(
        request_body=serializer_class,
        responses={200: serializer_class},
    )
    def put(self, request, *args, **kwargs):
        """
        Edit (overwrite) existing Employee data.

        This endpoint edit existing Employee identified by PK.
        """
        try:
            Company.objects.get(pk=request.data["company"])
        except Company.DoesNotExist:
            return Response(
                {
                    "errors": f"Company with id:{request.data['company']} does not exist.",
                    "status": status.HTTP_400_BAD_REQUEST,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        instance = get_object_or_404(Employee, pk=kwargs["pk"])
        serializer = self.serializer_class(instance, data=request.data)

        if serializer.is_valid():
            print(f"valid check{serializer.is_valid()}")
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

    @swagger_auto_schema(operation_summary="Partial update of an employee")
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)


class EmployeeDeleteApiView(generic_rest_views.DestroyAPIView):
    """
    Delete Employee here

    This endpoint delete employee, Employee is identified by PK.
    """

    queryset = Employee.objects.all()
    serializer_class = CreateEmployeeSerializer

    def destroy(self, request, *args, **kwargs):
        super().destroy(self, request, *args, **kwargs)
        return Response(
            {"status": status.HTTP_204_NO_CONTENT}, status=status.HTTP_204_NO_CONTENT
        )


class EmployeeDetailsApiView(generic_rest_views.RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializerWithCompany

    @swagger_auto_schema(
        responses={200: serializer_class},
    )
    def get(self, request, *args, **kwargs):
        """
        Retrieve Employee from DB.

        This endpoint shows Employee identified by PK.
        """
        try:
            instance = Employee.objects.get(pk=kwargs["pk"])
        except Employee.DoesNotExist:
            return Response(
                {"status": status.HTTP_404_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.get_serializer(instance)
        return Response(
            {"data": serializer.data, "status": status.HTTP_200_OK},
            status=status.HTTP_200_OK,
        )


class GetUserByToken(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        responses={200: "{'userNameByToken': 'Token Content' }"},
    )
    def get(self, request, format=None):
        """
        Retrieve current user's 'username' from DB.

        This endpoint shows current user's 'username' identified by Auth Token.
        """
        token_string = request.auth.pk
        content = {
            #  next two rows are used with basic accounts
            # 'user': str(request.user),  # `django.contrib.accounts.User` instance.
            # 'accounts': str(request.accounts),  # None
            "userNameByToken": str(Token.objects.get(key=token_string).user),
            # 'accounts': str(request.accounts),  # None
        }
        return Response(
            content,
            status=status.HTTP_200_OK,
        )


class RegisterView(generic_rest_views.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    @swagger_auto_schema(
        operation_summary="Register user here.",
        operation_description="This endpoint register user after necessary data is provided.",
        request_body=serializer_class,
    )
    def post(self, request):
        user = User(**request.data)
        user.set_password(user.password)
        try:
            user.save()
            # # Following row show what happen when there is ASYNC
            # # time.sleep(60)
            # # !!!! To run function through celery "delay" should be used as in the example below delay accept arguments!
            send_welcome_email_to_new_users.delay(user.username, user.email)
        except IntegrityError as ex:
            return Response({"message": f"{ex}"}, status=status.HTTP_409_CONFLICT)

        return Response(
            {"message": f"Successfully registered.<{user}>"},
            status=status.HTTP_201_CREATED,
        )


class LogOutUser(APIView):
    @swagger_auto_schema(
        responses={200: '{"success": f"Successfully logged out.<{user}>"}'},
    )
    def post(self, request):
        """
        Logging out current user

        This Logout current user, identified by Auth Token
        """
        # show it to Alex with debugger
        token_string = request.auth.pk
        user = str(Token.objects.get(key=token_string).user)
        try:
            request.user.auth_token.delete()
        except (AttributeError, ObjectDoesNotExist):
            pass

        # logout(request)

        return Response(
            {"success": f"Successfully logged out.<{user}>"}, status=status.HTTP_200_OK
        )


class CustomAuthToken(ObtainAuthToken):
    """
    Authenticate and Retrieve token from here ;).

    This endpoint authenticates the user and returns an authentication token.
    """

    @swagger_auto_schema(
        responses={
            200: openapi.Response(
                description="Successful authentication",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "token": openapi.Schema(type=openapi.TYPE_STRING),
                    },
                ),
            ),
            400: openapi.Response(
                description="Unsuccessful authentication",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "non_field_errors": openapi.Schema(
                            type=openapi.TYPE_ARRAY,
                            items=openapi.Schema(type=openapi.TYPE_STRING),
                        )
                    },
                ),
            ),
        },
    )
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return Response(
            {
                "token": token.key,
                # 'user_id': user.pk,
                # 'email': user.email
            },
            status=status.HTTP_200_OK,
        )


"""
Some crazy comments
Some crazy comments for second time
Some Crazy again
"""
