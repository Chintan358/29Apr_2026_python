from django.shortcuts import render
from rest_framework import viewsets
from eshop.models import *
from eshop.serializer import *
from rest_framework.response import Response
from rest_framework.decorators import action

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

    @action(detail=False,methods=['GET'],url_name="productbycategory")
    def productbycategory(self,request):
        id = request.GET['id']
        products = Product.objects.filter(category_id=id)
        ser = ProductSerializer(products,many=True)
        return Response({"data":ser.data})