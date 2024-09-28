from resources.ErrorMessage import ERROR_MESSAGE
from datetime import datetime


def create_error_message_object(error_message, status_code):
    errors = ERROR_MESSAGE.STATUS_TO_ERROR
    now = datetime.now()
    error_name = errors.get(status_code, 'Error')
    error_object = {
        'error': error_name,
        'status_code': status_code,
        'message': error_message,
        'timestamp': now.strftime("%Y-%m-%d %H:%M:%S")
    }
    return error_object