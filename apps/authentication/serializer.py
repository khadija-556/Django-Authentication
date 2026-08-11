from rest_framework import serializers
from .models import *

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        feilds = ['first_name','last_name','email','phone','photo_url','password','created_at']
        read_only = ['created_at']
        write_only = ['password']

        extra_kwargs = {
            'email': {'required': False },
            'first_name': {'required': False},
            'last_name': {'required': False},
            'phone': {'required': False},
            'photo_url':{'required':False},
            'password': {'write_only': True},
        }

        def to_representation(self,instance):
            representation = super().to_representation(instance)
            request = self.context.get('request')

        if request and instance.photo_url and hasattr(instance.photo_url, 'url'):
            representation['photo_url'] = request.build_absolute_uri(instance.photo_url.url)
        else:
            representation['photo_url'] = None
            
        return representation

        
        def create(self,validated_data):
            password = validated_data.pop('password')
            user = CustomUser(**validated_data)
            user.set_password(password)
            user.save()
            return user
    