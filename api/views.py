from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Products,Carts
from api.serializers import ProductModelSerializers,ProductSerializers,UserSerializers,CartSerializers

from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework.decorators import action
from django.contrib.auth.models import User
from rest_framework import authentication,permissions

class ProductView(APIView):
    def get(self,request,*args,**kwargs):
        qs=Products.objects.all()
        serializer=ProductSerializers(qs,many=True)
        return Response(data=serializer.data)
    
    def post(self,request,*args,**kwargs):
        serializer=ProductSerializers(data=request.data)
        if serializer.is_valid():
            print(serializer.validated_data)
            Products.objects.create(**serializer.validated_data)        
            return Response(data=serializer.data)
        else:
            return Response(serializer.errors)
        

class ProductdetailsView(APIView):
    def get(self,request,*args,**kwargs):
        print(kw)
        id=kw.get("id")
        qs=Products.objects.get(id=id)
        serializer=ProductSerializers(qs,many=False)
        return Response(data=serializer.data)
    
    
    def put(self,request,*args,**kwargs):
        id = kw.get('id')
        serializer = ProductSerializers(data=request.data)
        if serializer.is_valid():
            Products.objects.filter(id=id).update(**request.data)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
            
    

    def delete(self,request,*args,**kwargs):
        id=kw.get('id')
        Products.objects.filter(id=id).delete()
        return Response(data='delete a products')
    

# class ProductViewSetView(ViewSet):
#     def list(self,request,*args,**kwargs):
        
#         qs = Products.objects.all()
#         serializer = ProductSerializer(qs,many=True)
#         return Response(data=serializer.data)
            
#     def create(self,request,*args,**kwargs):
#         serializer = ProductModelSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data)
#         else:
#             return Response(data=serializer.errors)
        
#     def retrive(self,request,*args,**kwargs):
#         id=kw.get('pk')
#         qs = Products.objects.get(id=id)
#         serializer = ProductSerializer(data=request.data)
        
#         return Response(data=serializer.data)
        
#     def distroy(self,request,*args,**kwargs):
#         id=kw.get('pk')
#         Products.objects.filter(id=id).delete()
#         return Response(data='delete a products')
    
#     def update(self,request,*args,**kwargs):
#         id=kw.get('pk')
#         obj =Products.objects.get(id=id)
#         serializer =ProductModelSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data)
#         else:
#             return Response(data=serializer.errors)
        

#     @action(methods=['GET'],detail=False)
#     def categories(self,request,*args,**kwargs):
#         res = Products.objects.values_list('category',flat=True).distinct()
#         return Response(data=res)
    
    
#     @action(methods=['GET'],detail=False)
#     def discriptions(self,request,*args,**kwargs):
#         res = Products.objects.values_list('discription',flat=True).distinct()
#         return Response(data=res)
    
# class UserView(ViewSet):
#     def create(self,request,*argd,**kwargs):
#         serializer = UserSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data)
#         else:
#             return Response(data=serializer.errors)
        
class ProductModelviewset(ModelViewSet):
    serializer_class = ProductModelSerializers
    queryset = Products.objects.all()
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    @action(methods=['POST'],detail=True)
    def addto_cart(self,request,*args, **kwargs):
        id = kwargs.get("pk")
        item = Products.objects.get(id=id)
        user = request.user
        user.carts_set.create(product=item)
        return Response(data='item added to cart')
    
class CartView(ModelViewSet):
    serializer_class = CartSerializers
    queryset = Carts.objects.all()
    
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def list(self,request,*args, **kwargs):
        qs = request.user.carts_set.all()
        serializer = CartSerializers(qs,many=True)
        return Response(data=serializer.data)
   # def post(self,request,*args,**kwargs):
     #   id = kwargs.get("id")
      #  item = Products.objects.get(id=id)
      #  user = request.user
      #  user.carts_set.create(product=item)
       # return Response(data='item added to cart')
    
        
# class ModelUserView(ModelViewSet):
#     serializer_class = UserSerializers
#     queryset = User.objects.all()

    




