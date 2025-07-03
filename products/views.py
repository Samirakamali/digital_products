from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from .models import Category, Product, File
from .serializers import CategorySerializer, ProductSerializer, FileSerializer

class ProductListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        print(request.user)
        print(request.auth)
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True, context= {'request': request}) #  context= {'request': request}: for absoulute path

        return Response(serializer.data)
    
class ProductDetail(APIView):
    def get(self, request, pk):
        try:
            products = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
           return Response(status= status.HTTP_404_NOT_FOUND)
        
        serializer = ProductSerializer(products, context= {'request': request}) 

        return Response(serializer.data)
    
class CategoryListView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True, context= {'request': request}) 

        return Response(serializer.data)
    
class CategoryDetail(APIView):
    def get(self, request, pk):
        try:
            categories = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
           return Response(status= status.HTTP_404_NOT_FOUND)
        
        serializer = CategorySerializer(categories, context= {'request': request}) 

        return Response(serializer.data)
    

class FileListView(APIView):
    def get(self, request, *args, **kwargs):
        product_id = kwargs.get('product_id')
        files = File.objects.filter(product_id=product_id)
        serializer = FileSerializer(files, many=True, context={'request': request})
        return Response(serializer.data)
    
class FileDetail(APIView):
    def get(self, request, product_id, pk):
        try:
            files = File.objects.get(pk=pk, product_id=product_id)
        except File.DoesNotExist:
           return Response(status= status.HTTP_404_NOT_FOUND)
        
        serializer = FileSerializer(files, context= {'request': request}) 

        return Response(serializer.data)



# Create your views here.
