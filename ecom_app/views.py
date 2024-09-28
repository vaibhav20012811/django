from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.db import transaction

from resources.AllPurpose import AllPurpose
from resources.Logging import LoggingUtils

from . import helper


class EcomUserAPIView(APIView):
    def get(self, request):
        try:
            LoggingUtils.start_logger_info(self.get_view_name(), request.data)
            data, status_code = helper.get_ecom_user(request.data)
            return Response(data=data, status=status_code)
        except Exception as ex:
            LoggingUtils.exception_logger_info(self.get_view_name(), ex)
            data = AllPurpose.create_error_message_object(str(ex), status.HTTP_500_INTERNAL_SERVER_ERROR)
            return Response(data=data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @transaction.atomic
    def post(self, request):
        try:
            LoggingUtils.start_logger_info(self.get_view_name(), request.data)
            data, status_code = helper.save_ecom_user(request.data)
            return Response(data=data, status=status_code)
        except KeyError as ex:
            LoggingUtils.exception_logger_info(self.get_view_name(), ex)
            data = AllPurpose.create_error_message_object(f"KeyError: {str(ex)}", status.HTTP_400_BAD_REQUEST)
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            LoggingUtils.exception_logger_info(self.get_view_name(), ex)
            data = AllPurpose.create_error_message_object(str(ex), status.HTTP_500_INTERNAL_SERVER_ERROR)
            return Response(data=data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)