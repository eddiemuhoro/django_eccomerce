from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from product.models import Product  # Assuming the model is named Products

# Create your views here.
class ProductView(APIView):
    def get(self, request):
        try:
            products = Product.objects.all().values()
            if not products:
                return Response({"message": "No products found"}, status=404)
            return Response({"products": list(products)}, status=200)
        except:
            return Response({"error": "An error occurred while fetching products"}, status=500)
        
class CartView(APIView):
    def get(self, request):
        try:
            # Assuming you have a Cart model to fetch cart items
            cart_items = []  # Replace with actual cart fetching logic
            if not cart_items:
                return Response({"message": "No items in the cart"}, status=404)
            return Response({"cart_items": cart_items}, status=200)
        except:
            return Response({"error": "An error occurred while fetching cart items"}, status=500)