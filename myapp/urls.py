from django.urls import path
from . import views

urlpatterns = [
    path('', views.read_csv, name='read_csv'),
    path('campaign/', views.campaign, name='campaign'),
]
