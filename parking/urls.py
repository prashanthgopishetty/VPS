from django.urls import path

from parking import views

urlpatterns = [
    path('', views.home),
    path('getSlot', views.getSlotByCarNo),
    path('getCar', views.getCarNoBySlot)
]