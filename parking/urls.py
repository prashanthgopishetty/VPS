from django.urls import path
from parking import views

urlpatterns = [
    path('getCar/<int:carNo>', views.parking_slots)
]