from django.shortcuts import render
from orders.models import Order
from rest_framework.views import APIView
from rest_framework.response import Response
from orders.serializers import OrderSerializer
from product.models import Product

# Create your views here.
class OrderView(APIView):
    def get(self, request, *args, **kwargs):
        # Logic to retrieve and display orders
        orders = Order.objects.all()  # Assuming you have an Order model
        if not orders.exists():
            return Response({"message": "No orders found"}, status=404)
        serializer = OrderSerializer(orders, many=True)
        return Response({"orders": serializer.data}, status=200)

    def post(self, request, *args, **kwargs):
        # Logic to create a new order
        try:
            data = request.data
            product = Product.objects.get(id=data['product_id'])
            order = Order.objects.create(
                product=product,
                quantity=data['quantity'],
                price=data['price']
            )
            return Response({"message": "Order created successfully", "order_id": order.id}, status=201)
        except Exception as e:
            return Response({"error": str(e)}, status=400)