from rest_framework.serializers import ModelSerializer
from eshop.models import *

class CategorySerializer(ModelSerializer):
    class Meta : 
        model=Category
        fields = '__all__'
        
class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
    def to_representation(self, instance):
        resp = super().to_representation(instance)
        resp['category']=CategorySerializer(instance.category).data
        return resp