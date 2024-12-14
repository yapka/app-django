
from django.contrib import admin
from django.urls import path
from test_app import views

urlpatterns = [

path('', views.home),
path('create/', views.create, name='create'),
path('update/<int:pk>', views.update, name='update'),
path('delete/<int:pk>', views.delete, name='delete'),
]