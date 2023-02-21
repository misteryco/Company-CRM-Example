from rest_framework import generics as rest_views

from crm_for_companies.api_companies.models import Company
from crm_for_companies.api_companies.serializers import CompanySerializer


class CompanyListApiView(rest_views.ListAPIView):
    queryset = Company.objects.all()
    create_serializer_class = CompanySerializer
    list_serializer_class = CompanySerializer

    def get_serializer_class(self):

        for obj in self.queryset.all():
            print(obj.logo.url)

        if self.request.method == 'GET':
            return self.list_serializer_class
        return self.create_serializer_class
