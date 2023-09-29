from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Customer
from .serializers import CustomerSerializer
from django.contrib.sessions.models import Session
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

class CustomerRegistration(APIView):
    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            # Create a User object with the same email as the customer
            user = User.objects.create_user(
                username=serializer.validated_data['email'],
                password=serializer.validated_data['password']
            )
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomerLogin(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            customer = Customer.objects.get(email=email, password=password)
            serializer = CustomerSerializer(customer)
            user = User.objects.get(username=customer.email)  # Assuming email is the username
            login(request, user)
            # Include user data in the response
            user_data = serializer.data
            user_data['username'] = user.username  # Add username to user data
            return Response({'errorCode': '0', 'message': 'Login Successful', 'user': user_data}, status=status.HTTP_200_OK)
        except Customer.DoesNotExist:
            return Response({'errorCode': '1', 'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
