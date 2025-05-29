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