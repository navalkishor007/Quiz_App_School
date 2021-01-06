from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('exam/',views.exam),
]