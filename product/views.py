from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class ProductView(APIView):
    def get(self, request):
        try:
            products = [
                {"id": 1, "name": "Product 1", "price": 100.00, "description": "Description for product 1"},
                {"id": 2, "name": "Product 2", "price": 200.00, "description": "Description for product 2"},
                {"id": 3, "name": "Product 3", "price": 300.00, "description": "Description for product 3"},
            ]
            return Response({"products": products}, status=200)
        except:
            return Response({"error": "An error occurred while fetching products"}, status=500)