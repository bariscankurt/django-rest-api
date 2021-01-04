from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# third party imports.
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PostSerializer
from .models import Post
class TestView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            "name":"john",
            "age":"18",
            "job":"student"
        }
        return Response(data)
    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)
# def index(request):
#     data = {
#         "name":"john",
#         "age":"18",
#         "job":"student"
#     }
#     return JsonResponse(data)

