from rest_framework import generics as rest_views
import cloudinary.uploader
from rest_framework.response import Response

from crm_for_companies.api_employees.models import Employee
from crm_for_companies.api_employees.serializers import EmployeeSerializerWithCompany, CreateEmployeeSerializer


class EmployeeListApiView(rest_views.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializerWithCompany

    def get_queryset(self):
        company_id = self.request.query_params.get('company_id')
        queryset = self.queryset

        if company_id:
            queryset = queryset.filter(company_id=company_id)

        return queryset.all()


class EmployeeCreateApiView(rest_views.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = CreateEmployeeSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        file = request.data.get('photo')
        photo = cloudinary.uploader.upload(file)
        serializer.validated_data['photo'] = photo['url']
        serializer.save()

        return Response(serializer.data)


class EmployeeUpdateApiView(rest_views.RetrieveUpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = CreateEmployeeSerializer


class EmployeeDeleteApiView(rest_views.RetrieveDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = CreateEmployeeSerializer
