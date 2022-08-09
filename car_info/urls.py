from django.urls import path

from .views import Car_infoListView, Car_infoDetailView

urlpatterns = [
    path('', Car_infoListView.as_view(), name = 'car_info_list'),
    path('<int:pk>/', Car_infoDetailView.as_view(), name = 'car_info_detail'),
]