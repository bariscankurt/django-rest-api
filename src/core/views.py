from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# third party imports.
from rest_framework.response import Response
from rest_framework.views import APIView

class TestView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            "name":"john",
            "age":"18",
            "job":"student"
        }
        return Response(data)

# def index(request):
#     data = {
#         "name":"john",
#         "age":"18",
#         "job":"student"
#     }
#     return JsonResponse(data)