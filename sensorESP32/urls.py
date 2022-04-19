from django.urls import path
from sensorESP32 import views

urlpatterns = [
    path('cropRecommadationlist', views.recommadation_list),
    path('cropRecommadation', views.crop_recommendation),
    path('sensorESP32/', views.sensor_data_list),
    path('sensorESP32/<int:pk>', views.sensor_data_detail),
]
