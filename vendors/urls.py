from django.contrib import admin
from django.urls import path
from .views import VendorViewSet

urlpatterns = [
    path('', VendorViewSet.as_view({'get': 'list', 'post': 'create'}), name='vendor-list'),
    path('<int:pk>/', VendorViewSet.as_view({'get': 'retrieve', 'put': 'update'}), name='vendor-detail'),
    path('<int:pk>/delete/', VendorViewSet.as_view({'delete': 'destroy'}), name='vendor-delete'),
]





