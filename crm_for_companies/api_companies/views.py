import cloudinary.uploader
from django.shortcuts import get_object_or_404
from rest_framework import views as rest_basic_views, status
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework.response import Response
from rest_framework.settings import api_settings

from crm_for_companies.api_companies.models import Company
from crm_for_companies.api_companies.serializers import CompanySerializer, CompanyCreateSerializer, \
    CompanySerializerWithEmployees


class CompanyListApiView(rest_basic_views.APIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializerWithEmployees

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

    def get(self, request, pk):
        instance = self.serializer_class(get_object_or_404(Company, pk=pk))
        # print(f"get obj {instance}")
        # instance1 = self.serializer(self.queryset.filter(pk=pk).get())
        # print(f"int1{instance1}")
        return Response(instance.data)

    def put(self, request, pk):
        instance = get_object_or_404(Company, pk=pk)
        # instance = get_object_or_404(Company, pk=1)
        serializer = self.serializer_class(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data, 'errors': serializer.errors, 'status': status.HTTP_200_OK},
                            status=status.HTTP_200_OK, )
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
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

# class GenericCompanyListApiView(rest_views.ListCreateAPIView):
#     parser_classes = (
#         MultiPartParser,
#         JSONParser,
#     )
#
#     queryset = Company.objects.all()
#     # serializer_class = CompanySerializer
#
#     create_serializer_class = CompanySerializer
#     list_serializer_class = CompanySerializerWithEmployees
#
#     def get_queryset(self):
#         company_id = self.request.query_params.get('company_id')
#         queryset = self.queryset.all()
#         if company_id:
#             queryset = queryset.filter(id=company_id)
#         return queryset
#
#     def get_serializer_class(self):
#
#         # for obj in self.queryset.all():
#         #     print(obj.logo.url)
#
#         if self.request.method == 'GET':
#             return self.list_serializer_class
#         return self.create_serializer_class
#
#     def get(self, *args, **kwargs):
#         print()
#         return super().get(*args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         serializer_class = self.get_serializer_class()
#         serializer = serializer_class(data=request.data,
#                                       context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         file = request.data.get('logo')
#         logo = cloudinary.uploader.upload(file)
#         print(logo['url'])
#         serializer.validated_data['logo'] = logo['url']
#         serializer.save()
#
#         return Response(serializer.data)
#
#         # return Response({
#         #     'name': serializer.validated_data['name'],
#         #     'description': serializer.validated_data['description'],
#         #     'logo': serializer.validated_data['logo'],
#         # })
