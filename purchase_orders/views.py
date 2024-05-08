from django.shortcuts import render
from rest_framework import generics
from.models import PurchaseOrder
from .serializers import PurchaseOrder,PurchaseOrderSerializer
# Create your views here.

class PurchaseOrderListCreate(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class PurchaseOrderRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

