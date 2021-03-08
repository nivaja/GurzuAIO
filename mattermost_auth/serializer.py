from rest_framework import  serializers
from .models import MatthermostAuth

class MattermostAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatthermostAuth
        depth = 1
        fields = '__all__'