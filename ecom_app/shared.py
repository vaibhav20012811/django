
def basic_response_translator(is_success, data, total_count=None, start=None, end=None):
    response_translator = {}
    response_translator["success"] = is_success
    if total_count:
        response_translator["total_count"] = total_count
    elif total_count == 0:
        response_translator["total_count"] = total_count
    if start:
        response_translator["start"] = start
    elif start == 0:
        response_translator["start"] = start
    if end:
        response_translator["end"] = end
    elif end == 0:
        response_translator["end"] = end
    response_translator["data"] = data
    return response_translator