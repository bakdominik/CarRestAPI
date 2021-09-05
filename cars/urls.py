from django.urls import path, include
from . import views

urlpatterns = [
    path('cars/',views.cars, name='cars'),
    path('cars/<pk>/',views.cars, name='cars'),
    path('popular/',views.popular, name='popular'),
    path('rate/',views.rate, name='rate'),
]