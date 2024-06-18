from rest_framework import serializers
from api.models import Products,Carts
from django.contrib.auth.models import User

class ProductSerializers(serializers.Serializer):

    name = serializers.CharField()
    price = serializers.IntegerField()
    description = serializers.CharField()
    category = serializers.CharField()
    image = serializers.ImageField

class ProductModelSerializers(serializers.ModelSerializer):

   class Meta:
       
       model = Products
       fields = "__all__"

class UserSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']

    def create(self,validated_data):
        return User.objects.create_user(**validated_data)
    
class CartSerializers(serializers.ModelSerializer):
    
    id = serializers.CharField(read_only=True)
    user = serializers.CharField(read_only=True)
    product = serializers.CharField(read_only=True)
    date = serializers.CharField(read_only=True) 
        
    class Meta:
        model = Carts
        fields = "__all__"
         
               