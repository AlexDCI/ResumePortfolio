

def middleware(get_response):
    def inner_middleware(request):
        response = get_response(request)
        return response
    return inner_middleware



class Middleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response
