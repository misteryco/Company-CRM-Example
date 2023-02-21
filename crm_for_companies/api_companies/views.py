import cloudinary.uploader
from rest_framework import generics as rest_views
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework.response import Response

from crm_for_companies.api_companies.models import Company
from crm_for_companies.api_companies.serializers import CompanySerializer


class CompanyListApiView(rest_views.ListCreateAPIView):
    parser_classes = (
        MultiPartParser,
        JSONParser,
    )

    queryset = Company.objects.all()
    # serializer_class = CompanySerializer

    create_serializer_class = CompanySerializer
    list_serializer_class = CompanySerializer

    def get_serializer_class(self):

        # for obj in self.queryset.all():
        #     print(obj.logo.url)

        if self.request.method == 'GET':
            return self.list_serializer_class
        return self.create_serializer_class

    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data,
                                      context={'request': request})
        serializer.is_valid(raise_exception=True)
        file = request.data.get('logo')
        logo = cloudinary.uploader.upload(file)
        # print(logo)
        serializer.validated_data['logo'] = logo['url']
        serializer.save()

        return Response({
            'name': serializer.validated_data['name'],
            'description': serializer.validated_data['description'],
            'logo': serializer.validated_data['logo'],
        })

    # def get_queryset(self):
    #     department_id = self.request.query_params.get('department_id')
    #     queryset = self.queryset
    #
    #     if department_id:
    #         queryset = queryset.filter(department_id=department_id)
    #
    #     return queryset.all()


# a = {'asset_id': '7f996cee5d546a10bb0a4e67765dcdfe',
#      'public_id': 'zsze5vu8xkxyptievfcx',
#      'version': 1676987189,
#      'version_id': '9b39a0f213807b21c6407261b113b706',
#      'signature': '7c7d442eb21351ba45c00b5cc4a2cc7fb67d046c',
#      'width': 1920,
#      'height': 1080, 'format': 'jpg', 'resource_type': 'image', 'created_at': '2023-02-21T13:46:29Z',
#      'tags': [],
#      'bytes': 1191771, 'type': 'upload', 'etag': '1bbd8ef78e125cf5c343566d9f2616ee',
#      'placeholder': False,
#      'url': 'http://res.cloudinary.com / dmpj1vv89 / image / upload / v1676987189 / zsze5vu8xkxyptievfcx.jpg',
#      'secure_url': 'https: // res.cloudinary.com / dmpj1vv89 / image / upload / v1676987189 / zsze5vu8xkxyptievfcx.jpg',
#      'folder': '', 'original_filename': '03', 'api_key': '561138945368434'
#      }
