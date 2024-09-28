from . import models, serializers, validation
from rest_framework import status
from resources.Exceptions import ProductConfiguratorCustomException
from resources.ErrorMessage import ERROR_MESSAGE
from django.db import transaction
from .shared import basic_response_translator

def get_ecom_user(data):
    limit = data.get("limit", 0)
    offset = data.get("offset", 10)

    user_count = models.EcomUser.objects.all().order_by("-id").count()
    users = models.EcomUser.objects.all().order_by("-id")[limit:offset]

    if not users:
        return [], status.HTTP_200_OK
    
    serializer = serializers.EcomUserSerializer(users, many=True).data
    data = basic_response_translator(True, serializer, total_count=user_count)
    return data, status.HTTP_200_OK

@transaction.atomic
def save_ecom_user(data):
    if not data:
        return ERROR_MESSAGE.ECOM_USER_DATA_INVALID, status.HTTP_400_BAD_REQUEST

    user_obj = {
        "name": data["name"],
        "city": data["city"],
        "state": data["state"]
    }
    ecom_user_serializer = serializers.EcomUserSerializer(data=user_obj)

    if ecom_user_serializer.is_valid():
        ecom_user_serializer.save()
    else:
        raise ProductConfiguratorCustomException.ProductConfiguratorException(
            error_message=ERROR_MESSAGE.ECOM_USER_DATA_INVALID,
            status_code=status.HTTP_406_NOT_ACCEPTABLE)
    return ERROR_MESSAGE.ECOM_USER_SAVED, status.HTTP_201_CREATED

def update_ecom_user(data):
    pass