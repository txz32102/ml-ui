# from django.http import HttpResponse


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

from django.http import JsonResponse

def index(request):
    data = {
        'name': 'John Doe',
        'age': 30,
        'email': 'john.doe@example.com'
    }
    response = JsonResponse(data, status=200)
    return response