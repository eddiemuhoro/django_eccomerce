from django.shortcuts import render
from orders.models import Order
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class OrderView(APIView):
    def get(self, request, *args, **kwargs):
        # Logic to retrieve and display orders
        orders = Order.objects.all()  # Assuming you have an Order model
        if not orders:
            return Response({"message": "No orders found"}, status=404)
        return Response({"orders": list(orders.values())}, status=200)