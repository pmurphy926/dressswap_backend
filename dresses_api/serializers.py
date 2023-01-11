from rest_framework import serializers 
from .models import Dress 

class DressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dress
        fields = ('id', 'color', 'brand', 'styles', 'size', 'imageURL', 'image2URL', 'image3URL',)
