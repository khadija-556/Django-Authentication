from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .response import base_error_response, base_success_response, Codenco

# Create your views here.

class UserRegistration(APIView):
    def post(self,request):
        data = request.data

        if data.get('password') != data.get('confirm_password'):
            return Response(base_error_response("Passwords do not match"),
                            status= status.HTTP_400_BAD_REQUEST)
    
        if not data.get('email'):
            return Response(base_error_response("Email is Required"))
        
        if CustomUser.objects.filter(email = data.get('email')).exists():
            return Response(base_error_response("Email already exists"))

        serializer = UserRegistrationSerializer(data=data, context={'request':request})

        if serializer.is_valid():
            serializer.save()

            user = serializer.instance

            return Response(
                base_success_response(
                    "User Registered Successfully",
                    data=serializer.data
                ),
                status=status.HTTP_201_CREATED
            )

        return Response(
            base_error_response(
                "Serializer Error",
                errors=serializer.errors
            ),
            status=status.HTTP_400_BAD_REQUEST
        )
