from django.shortcuts import get_object_or_404
from rest_framework import generics as generic_rest_views, views as rest_basic_views, status, permissions
import cloudinary.uploader
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from crm_for_companies.api_companies.models import Company
from crm_for_companies.api_employees.models import Employee
from crm_for_companies.api_employees.serializers import EmployeeSerializerWithCompany, CreateEmployeeSerializer


class EmployeeListApiView(rest_basic_views.APIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializerWithCompany

    def get(self, request):
        serializer = self.serializer_class(self.get_queryset(), many=True)

        return Response({'data': serializer.data, 'status': status.HTTP_200_OK},
                        status=status.HTTP_200_OK, )

    def get_queryset(self):
        company_id = self.request.query_params.get('company_id')
        queryset = self.queryset

        if company_id:
            queryset = queryset.filter(company_id=company_id)

        return queryset.all()


class EmployeeCreateApiView(rest_basic_views.APIView):
    queryset = Employee.objects.all()
    serializer_class = CreateEmployeeSerializer

    def post(self, request, *args, **kwargs):

        try:
            Company.objects.get(pk=request.data['company'])
        except Company.DoesNotExist:
            return Response({'errors': f"Company with id:{request.data['company']} does not exist.",
                             'status': status.HTTP_400_BAD_REQUEST},
                            status=status.HTTP_400_BAD_REQUEST)

        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})

        if serializer.is_valid(raise_exception=True):
            file = request.data.get('photo')
            photo = cloudinary.uploader.upload(file)
            serializer.validated_data['photo'] = photo['url']
            serializer.save()
            return Response({'data': serializer.data, 'errors': serializer.errors, 'status': status.HTTP_201_CREATED},
                            status=status.HTTP_201_CREATED, )

        return Response({'errors': serializer.errors, 'status': status.HTTP_400_BAD_REQUEST},
                        status=status.HTTP_400_BAD_REQUEST)


class EmployeeUpdateApiView(generic_rest_views.RetrieveUpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = CreateEmployeeSerializer

    def put(self, request, *args, **kwargs):
        try:
            Company.objects.get(pk=request.data['company'])
        except Company.DoesNotExist:
            return Response({'errors': f"Company with id:{request.data['company']} does not exist.",
                             'status': status.HTTP_400_BAD_REQUEST},
                            status=status.HTTP_400_BAD_REQUEST)

        instance = get_object_or_404(Employee, pk=kwargs['pk'])
        serializer = self.serializer_class(instance, data=request.data)

        if serializer.is_valid():
            print(f"valid check{serializer.is_valid()}")
            serializer.save()
            return Response({'data': serializer.data, 'errors': serializer.errors, 'status': status.HTTP_200_OK},
                            status=status.HTTP_200_OK, )

        return Response({'errors': serializer.errors, 'status': status.HTTP_400_BAD_REQUEST},
                        status=status.HTTP_400_BAD_REQUEST)


class EmployeeDeleteApiView(generic_rest_views.RetrieveDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = CreateEmployeeSerializer

    def destroy(self, request, *args, **kwargs):
        super().destroy(self, request, *args, **kwargs)
        return Response({'status': status.HTTP_204_NO_CONTENT}, status=status.HTTP_204_NO_CONTENT)


class EmployeeDetailsApiView(generic_rest_views.RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializerWithCompany

    def get(self, request, *args, **kwargs):
        try:
            instance = Employee.objects.get(pk=kwargs['pk'])
        except Employee.DoesNotExist:
            return Response({'status': status.HTTP_404_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(instance)
        return Response({'data': serializer.data,
                         'status': status.HTTP_200_OK},
                        status=status.HTTP_200_OK, )


class GetUserByToken(APIView):
    # following rows are used when we have not configured settings file with : DEFAULT_AUTHENTICATION_CLASSES
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]

    def get(self, request, format=None):
        # show it to Alex with debugger
        token_string = request.auth.pk
        content = {
            #  next two rows are used with basic auth
            # 'user': str(request.user),  # `django.contrib.auth.User` instance.
            # 'auth': str(request.auth),  # None
            'userNameByToken': str(Token.objects.get(key=token_string).user),
            # 'auth': str(request.auth),  # None
        }
        return Response(content)
