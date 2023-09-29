from django.shortcuts import render
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from .models import BtsFashion, BtsAlbum, BT21
from .serializers import BtsFashionSerializer, BtsAlbumSerializer, BT21Serializer
from rest_framework.views import APIView

class BtsFashionList(APIView):
    def get(self, request):
        bts_fashion_data = BtsFashion.objects.all()
        serialized_data = [
            {
                'imgURL': item.image.url,
                'price': item.price,
                'itemName': item.name,
            }
            for item in bts_fashion_data
        ]
        return Response(serialized_data)

class BtsAlbumList(generics.ListAPIView):
    queryset = BtsAlbum.objects.all()
    serializer_class = BtsAlbumSerializer

class BT21List(generics.ListAPIView):
    queryset = BT21.objects.all()
    serializer_class = BT21Serializer
