from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bill/', views.produce_bill, name='produce_bill'),
]
