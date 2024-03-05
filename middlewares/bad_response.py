
from django.http import JsonResponse

class ResponseMiddlewareFor404:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Check if the response has a 404 status code
        if response.status_code == 404:
            return JsonResponse({'detail': 'Not Found'}, status=404)

        return response
    
    