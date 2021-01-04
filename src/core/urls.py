from django.urls import path

from core.views import TestView

urlpatterns = [
    path('api/', TestView.as_view(), name='test'),
]