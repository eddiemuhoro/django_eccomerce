from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductView, CartView

router = DefaultRouter()
urlpatterns = [
    path('', ProductView.as_view(), name='product-list'),
    path('cart/', CartView.as_view(), name='cart')
]