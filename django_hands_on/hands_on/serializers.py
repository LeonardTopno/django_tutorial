from rest_framework import serializers
from .models import Drink

class DrinkSerializer(serializers.ModelSerializer):
    class Meta: #Innerclass Meta
        model = Drink
        
        #fieds = ['id', 'name', 'description'] 
        
        fields = '__all__'
 