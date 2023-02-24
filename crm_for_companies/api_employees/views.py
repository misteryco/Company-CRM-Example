from django.shortcuts import get_object_or_404
from rest_framework import generics as generic_rest_views, views as rest_basic_views, status
import cloudinary.uploader
from rest_framework.response import Response

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


# class GenericEmployeeListApiView(rest_views.ListAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializerWithCompany
#
#     def get_queryset(self):
#         company_id = self.request.query_params.get('company_id')
#         queryset = self.queryset
#
#         if company_id:
#             queryset = queryset.filter(company_id=company_id)
#
#         return queryset.all()


class EmployeeCreateApiView(rest_basic_views.APIView):
    queryset = Employee.objects.all()
    serializer_class = CreateEmployeeSerializer

    # TODO: Wrong company pk raise validation error
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        if serializer.is_valid(raise_exception=True):
            file = request.data.get('photo')
            photo = cloudinary.uploader.upload(file)
            serializer.validated_data['photo'] = photo['url']
            serializer.save()
            return Response({'data': serializer.data, 'errors': serializer.errors, 'status': status.HTTP_201_CREATED},
                            status=status.HTTP_201_CREATED, )

        return Response({'errors': serializer.errors, 'status': status.HTTP_400_BAD_REQUEST})


class EmployeeUpdateApiView(generic_rest_views.RetrieveUpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = CreateEmployeeSerializer

    # TODO: Use same serializer as create
    def put(self, request, *args, **kwargs):
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
