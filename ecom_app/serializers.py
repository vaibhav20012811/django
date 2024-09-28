from rest_framework import serializers
from .models import EcomUser

class EcomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = EcomUser
        fields = ['name', 'city', 'state']
