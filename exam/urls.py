from django.urls import path, include
from . import views

urlpatterns = [
    path(' ', views.exams, name="exams"),#exam researcher view to be created next
]