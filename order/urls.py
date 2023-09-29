# order/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.OrderCreateView.as_view(), name='order-create'),
    path('list/', views.OrderListView.as_view(), name='order-list'),
]
