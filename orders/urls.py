from django.urls import path
from orders.views import OrderView

urlpatterns = [
    path('', OrderView.as_view(), name='order-list'),
    path('<int:pk>/', OrderView.as_view(), name='order-detail'),
]
