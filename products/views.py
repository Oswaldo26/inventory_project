from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, filters
from .models import Product
from rest_framework.response import Response
from rest_framework import status
from .serializers.productSerializer import ProductSerializer
from rest_framework.views import APIView


class ListProductsView(APIView):
    """
    Vista para listar todos los productos.
    """
    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class RegisterProductView(APIView):
    """
    Vista para registrar un nuevo producto.
    """
    def post(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FilterProductsByCategoryView(APIView):
    """
    Vista para filtrar productos por categoría.
    """
    def get(self, request, *args, **kwargs):
        category = request.query_params.get('category', None)
        if category is not None:
            products = Product.objects.filter(category__icontains=category)
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "Category parameter is required."}, status=status.HTTP_400_BAD_REQUEST)

