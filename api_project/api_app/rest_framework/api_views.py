from .serializer import *
from rest_framework import viewsets
from rest_framework.response import Response
from api_app.models import *


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        product = Product.objects.all()
        return product

    def create(self,request,*args,**kwargs):
        data = request.data
        new_product = Product.objects.create(
            name=data['name'], image=data['image'], cash_on_delivery=data['cash_on_delivery'])
        new_product.save()
        for category in data['category']:
            category_obj = Category.objects.get(category=category['category'])
            new_product.category.add(category_obj)
        
        serializer = ProductSerializer(new_product)

        return Response(serializer.data)
    
    def update(self, request,*args,**kwargs):
        data = request.data
        get_primary_key = kwargs['pk']
        get_product = Product(id=get_primary_key, name=data['name'], image=data['image'], cash_on_delivery=data['cash_on_delivery'])
        get_product.save()
        category_list = []
        for category in data['category']:
            category_obj = Category.objects.get(category=category['category'])
            category_list.append(category_obj.id)
        get_product.category.set(category_list)

        serializer = ProductSerializer(get_product)

        return Response(serializer.data)
            
