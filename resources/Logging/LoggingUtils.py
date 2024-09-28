import logging
from rest_framework.response import Response
from rest_framework import status
from resources.ErrorMessage import ERROR_MESSAGE

# Get an instance of the logger
logger = logging.getLogger(__name__)


def start_logger_info(view, request):
    logger.info("{} started....".format(view))
    logger.info(request)
    return True


def end_logger_info(view, response):
    logger.info("{} ended....".format(view))
    logger.info(response)
    return True


def exception_logger_info(view, exception):
    logger.exception(exception)
    logger.exception(f"Exception raised in {view} as {exception}.")
    return True


def main_exception(view, exception, error_message=None):
    logger.error(exception)
    logger.exception("Exception raised in {} as {}".format(view, str(exception)))
    if error_message:
        return Response(error_message, status=status.HTTP_412_PRECONDITION_FAILED)
    return Response(ERROR_MESSAGE.GENERIC_API_FAILURE, status=status.HTTP_500_INTERNAL_SERVER_ERROR)