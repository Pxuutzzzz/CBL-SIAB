from django.urls import path
from . import views

app_name = 'stock_prediction'

urlpatterns = [
    path('', views.index, name='index'),
    path('predict/manual/', views.predict_manual, name='predict_manual'),
    path('predict/csv/', views.predict_csv, name='predict_csv'),
    path('predictions/', views.predictions_list, name='predictions_list'),
    path('visualize/', views.visualize, name='visualize'),
    path('api/predict/', views.api_predict, name='api_predict'),
]
