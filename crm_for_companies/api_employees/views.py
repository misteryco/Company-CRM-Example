from rest_framework import generics as rest_views

from crm_for_companies.api_employees.models import Employee
from crm_for_companies.api_employees.serializers import EmployeeSerializer


class EmployeeListApiView(rest_views.ListAPIView):
    queryset = Employee.objects.all()
    create_serializer_class = EmployeeSerializer
    list_serializer_class = EmployeeSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return self.list_serializer_class
        return self.create_serializer_class
