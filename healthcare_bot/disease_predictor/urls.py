# disease_predictor/urls.py
from django.urls import path
from .views import predict_request

urlpatterns = [
    path('predict/', predict_request, name='predict_request'),
]
