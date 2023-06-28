from django.contrib.auth import get_user_model
from drf_yasg import openapi

UserModel = get_user_model()


def get_first_user_pk():
    user = UserModel.objects.all().first()

    if user is not None:
        return user.pk
    else:
        return None


company_request_body_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "owner": openapi.Schema(
            type=openapi.TYPE_ARRAY,
            items=openapi.Items(type=openapi.TYPE_INTEGER),
        ),
        "name": openapi.Schema(type=openapi.TYPE_STRING),
        "description": openapi.Schema(type=openapi.TYPE_STRING),
        "logo": openapi.Schema(type=openapi.TYPE_STRING),
    },
    required=["owner", "name", "description", "logo"],
    example={
        "name": "Example Company",
        "description": "Some example company description",
        "logo": "/home/yd/Screenshot-10.png",
        "owner": [
            get_first_user_pk(),
        ],
    },
)

details_company_api_views_manual_parameters = [
    openapi.Parameter(
        "id",
        openapi.IN_PATH,
        description="id of the company to edit",
        type=openapi.TYPE_INTEGER,
        example=501,
    )
]
