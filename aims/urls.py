"""aims URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
"""
from django.conf.urls.static import static
from aims import settings
from django.urls import path, include

urlpatterns = [
    path('', include('aimsbackend.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
