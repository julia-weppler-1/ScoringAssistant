# excel_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_excel, name='upload_excel'),
    path('download-template/', views.download_template, name='download_template'),
    # Add more URL patterns for additional views if needed
]
