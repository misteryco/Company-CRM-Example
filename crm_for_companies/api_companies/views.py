import cloudinary.uploader
from rest_framework import generics as rest_views, views as rest_basic_views, status
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework.response import Response
from rest_framework.settings import api_settings

from crm_for_companies.api_companies.models import Company
from crm_for_companies.api_companies.serializers import CompanySerializer, CompanyCustomCreateSerializer


class CustomCompanyListApiView(rest_basic_views.APIView):
    queryset = Company.objects.all()

    def get(self, request):
        serializer = CompanySerializer(self.get_queryset(), many=True)

        return Response(serializer.data)

    def get_queryset(self):
        company_id = self.request.query_params.get('company_id')
        queryset = self.queryset.all()
        if company_id:
            queryset = queryset.filter(id=company_id)
        return queryset


class CustomCreateCompanyApiView(rest_basic_views.APIView):
    queryset = Company.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = CompanyCustomCreateSerializer(data=request.data,
                                                   context={'request': request})
        serializer.is_valid(raise_exception=True)
        file = request.data.get('logo')
        logo = cloudinary.uploader.upload(file)
        serializer.validated_data['logo'] = logo['url']
        serializer.save()

        return Response(serializer.data)

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}


class CustomDeleteCompanyApiView(rest_basic_views.APIView):
    pass


class CompanyListApiView(rest_views.ListCreateAPIView):
    parser_classes = (
        MultiPartParser,
        JSONParser,
    )

    queryset = Company.objects.all()
    # serializer_class = CompanySerializer

    create_serializer_class = CompanySerializer
    list_serializer_class = CompanySerializer

    def get_queryset(self):
        company_id = self.request.query_params.get('company_id')
        queryset = self.queryset.all()
        if company_id:
            queryset = queryset.filter(id=company_id)
        return queryset

    def get_serializer_class(self):

        # for obj in self.queryset.all():
        #     print(obj.logo.url)

        if self.request.method == 'GET':
            return self.list_serializer_class
        return self.create_serializer_class

    def get(self, *args, **kwargs):
        print()
        return super().get(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data,
                                      context={'request': request})
        serializer.is_valid(raise_exception=True)
        file = request.data.get('logo')
        logo = cloudinary.uploader.upload(file)
        print(logo['url'])
        serializer.validated_data['logo'] = logo['url']
        serializer.save()

        return Response(serializer.data)

        # return Response({
        #     'name': serializer.validated_data['name'],
        #     'description': serializer.validated_data['description'],
        #     'logo': serializer.validated_data['logo'],
        # })
