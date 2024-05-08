from django.urls import path
from.views import PurchaseOrderListCreate, PurchaseOrderRetrieveUpdateDestroy
# purchase_orders/urls.py

urlpatterns = [
    path('', PurchaseOrderListCreate.as_view(), name='purchase_order_list_create'),
    path('<int:pk>/', PurchaseOrderRetrieveUpdateDestroy.as_view(), name='purchase_order_retrieve_update_destroy'),
]
