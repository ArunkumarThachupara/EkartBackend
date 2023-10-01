from rest_framework import generics
from .models import Orders
from .serializers import OrderSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class OrderCreateView(APIView):
    serializer_class = OrderSerializer
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            # Create a new Order instance and save it to the database
            serializer.save()
            return Response({'errorCode': '0', 'message': 'Order Placed Successfully', 'user': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderListView(APIView):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer
