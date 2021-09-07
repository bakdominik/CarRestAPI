from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view
from . import views

urlpatterns = [
    path('cars/',views.cars, name='cars'),
    path('cars/<pk>/',views.car_delete, name='car_delete'),
    path('popular/',views.popular, name='popular'),
    path('rate/',views.rate, name='rate'),
    path('', get_schema_view(
            title="Cars REST API",
            description="API for rating cars",
            version="1.0.0"
        ), name='openapi-schema'),
]
