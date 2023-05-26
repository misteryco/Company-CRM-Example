import cloudinary.uploader
from django.shortcuts import get_object_or_404
from rest_framework import views as rest_basic_views, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from rest_framework.response import Response

from crm_for_companies.api_companies.models import Company, UserModel
from crm_for_companies.api_companies.serializers import CompanySerializer, CompanyCreateSerializer, \
    CompanySerializerWithEmployees


class IsCompanyOwner(BasePermission):
    message = 'List companies not allowed.'

    def has_permission(self, request, view):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False
        # Allow access for superusers
        if request.user.is_superuser:
            return True
        # Allow access if the user is the owner of the book
        if request.method in SAFE_METHODS:
            return True

        return False

    def has_object_permission(self, request, view, obj):
        print("in_has_object_permission")
        # Allow access for superusers
        if request.user.is_superuser:
            return True
        # Following row is query in Django that retrieves instances of the UserModel where the related company has an
        # owner attribute that matches the request.user.
        return request.user in UserModel.objects.filter(company__owner=request.user)


class CompanyListApiView(rest_basic_views.APIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializerWithEmployees
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        serializer = self.serializer_class(self.get_queryset(), many=True)

        return Response({'data': serializer.data, 'status': status.HTTP_200_OK},
                        status=status.HTTP_200_OK, )

    def get_queryset(self):
        company_id = self.request.query_params.get('company_id')
        queryset = self.queryset.all()
        if company_id:
            queryset = queryset.filter(id=company_id)
        return queryset


class CreateCompanyApiView(rest_basic_views.APIView):
    queryset = Company.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = CompanyCreateSerializer(data=request.data,
                                             context={'request': request})
        if serializer.is_valid(raise_exception=True):
            file = request.data.get('logo')
            logo = cloudinary.uploader.upload(file)
            serializer.validated_data['logo'] = logo['url']
            serializer.save()
            return Response({'data': serializer.data, 'errors': serializer.errors, 'status': status.HTTP_201_CREATED},
                            status=status.HTTP_201_CREATED, )

        return Response({'errors': serializer.errors, 'status': status.HTTP_400_BAD_REQUEST})


class DetailsCompanyApiView(rest_basic_views.APIView):
    http_method_names = ['get', 'delete', 'put']
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    permission_classes = (IsCompanyOwner,)

    def get(self, request, pk):
        instance = self.serializer_class(get_object_or_404(Company, pk=pk))
        self.check_object_permissions(self.request, instance)

        return Response(instance.data)

    def put(self, request, pk):
        instance = get_object_or_404(Company, pk=pk)

        serializer = self.serializer_class(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data, 'errors': serializer.errors, 'status': status.HTTP_200_OK},
                            status=status.HTTP_200_OK, )

        return Response({'errors': serializer.errors, 'status': status.HTTP_400_BAD_REQUEST},
                        status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            instance = Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            return Response({'status': status.HTTP_404_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
        # instance = self.queryset.filter(pk=pk).get()
        instance.delete()
        return Response({'status': status.HTTP_204_NO_CONTENT}, status=status.HTTP_204_NO_CONTENT)
