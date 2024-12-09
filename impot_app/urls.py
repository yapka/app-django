
from django.urls import path, include
from impot_app import views


urlpatterns = [
    
    path('impot/', views.impot),
]
