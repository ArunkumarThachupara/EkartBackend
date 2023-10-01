from django.shortcuts import render
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from .models import BtsFashion, BtsAlbum, BT21
from .serializers import BtsFashionSerializer, BtsAlbumSerializer, BT21Serializer, BTSMechSerializer
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

class BTSFashionSearchAPIView(generics.ListAPIView):
    serializer_class = BtsFashionSerializer
    def get_queryset(self):
        query = self.request.query_params.get('query', '')
        btsFashion = [
        {
        'imgURL': "../assets/BTSFashion/1.jpg",
        'price': 1500,
        'itemName': "Namjoon's Vogue Bottega Venetta Shirt",
        },
        {
        'imgURL': "../assets/BTSFashion/2.jpg",
        'price': 1800,
        'itemName': "Seokjin's Astronaut Interview Shirt",
        },
        {
        'imgURL': "../assets/BTSFashion/3.jpg",
        'price': 1200,
        'itemName': "Yoongi's Yet To Come Concert Shirt",
        },
        {
        'imgURL': "../assets/BTSFashion/4.jpg",
        'price': 1700,
        'itemName': "Jhope's The Dance Kid Shirt",
        },
        {
        'imgURL': "../assets/BTSFashion/5.jpg",
        'price': 1400,
        'itemName': "Jimin's Run BTS TShirt",
        },
        {
        'imgURL': "../assets/BTSFashion/6.jpg",
        'price': 1900,
        'itemName': "Taehyung's Spongebob-Fred Outfit",
        },
        {
        'imgURL': "../assets/BTSFashion/7.jpg",
        'price': 1100,
        'itemName': "Jungkook's OutFit on PTD LV Concert",
        },
        {
        'imgURL': "../assets/BTSFashion/8.jpg",
        'price': 1300,
        'itemName': "Namjoon's Balenciaga Black & White Shirt",
        },
        {
        'imgURL': "../assets/BTSFashion/9.jpg",
        'price': 1600,
        'itemName': "Jin's Pragmatic TShirt",
        },
        {
        'imgURL': "../assets/BTSFashion/10.jpg",
        'price': 2000,
        'itemName': "Yoongi's LV TShirt",
        },
        {
        'imgURL': "../assets/BTSFashion/11.jpg",
        'price': 1700,
        'itemName': "Hobi's Smiley Shirt",
        },
        {
        'imgURL': "../assets/BTSFashion/12.jpg",
        'price': 1500,
        'itemName': "Jimin's Dior Shirt",
        },
        {
        'imgURL': "../assets/BTSFashion/13.jpg",
        'price': 1800,
        'itemName': "Taehyung's Airport Fashion",
        },
        {
        'imgURL': "../assets/BTSFashion/14.jpg",
        'price': 1900,
        'itemName': "JK for CK",
        }
        ]
        results = []
        for product in btsFashion:
            if query.lower() in product['itemName'].lower():
                results.append(product)
        return results

class BTSAlbumsSearchAPIView(generics.ListAPIView):
    serializer_class = BtsAlbumSerializer
    def get_queryset(self):
        query = self.request.query_params.get('query', '')
        btsAlbums = [
    {
      'imgURL': "../assets/BTSAlbums/1.jpg",
      'price': 1500,
      'itemName': "Proof Album",
    },
    {
      'imgURL': "../assets/BTSAlbums/2.jpg",
      'price': 1800,
      'itemName': "My Universe",
    },
    {
      'imgURL': "../assets/BTSAlbums/3.jpg",
      'price': 1200,
      'itemName': "Butter",
    },
    {
      'imgURL': "../assets/BTSAlbums/4.jpg",
      'price': 1700,
      'itemName': "BE",
    },
    {
      'imgURL': "../assets/BTSAlbums/5.jpg",
      'price': 1400,
      'itemName': "Skool Luv Affair",
    },
    {
      'imgURL': "../assets/BTSAlbums/6.jpg",
      'price': 1900,
      'itemName': "Love Yourself Answer",
    },
    {
      'imgURL': "../assets/BTSAlbums/7.jpg",
      'price': 1100,
      'itemName': "BTS World",
    },
    {
      'imgURL': "../assets/BTSAlbums/8.jpg",
      'price': 1300,
      'itemName': "Map Of The Soul Persona",
    },
    {
      'imgURL': "../assets/BTSAlbums/9.jpg",
      'price': 1600,
      'itemName': "Dark & Wild",
    },
    {
      'imgURL': "../assets/BTSAlbums/10.jpg",
      'price': 2000,
      'itemName': "2CoolForSkool",
    },
    {
      'imgURL': "../assets/BTSAlbums/11.jpg",
      'price': 1700,
      'itemName': "Skool Luv Affair",
    },
    {
      'imgURL': "../assets/BTSAlbums/12.jpg",
      'price': 1500,
      'itemName': "O!RUL82?",
    },
    {
      'imgURL': "../assets/BTSAlbums/13.jpg",
      'price': 1800,
      'itemName': "Most Beautiful Moment in Life",
    },
    {
      'imgURL': "../assets/BTSAlbums/14.jpg",
      'price': 1900,
      'itemName': "Young Forever",
    },
    {
        'imgURL': "../assets/BTSAlbums/15.jpg",
        'price': 1900,
        'itemName': "Love Yourself Her",
    },
    {
        'imgURL': "../assets/BTSAlbums/16.jpg",
        'price': 1900,
        'itemName': "Wings",
    },
    {
        'imgURL': "../assets/BTSAlbums/17.jpg",
        'price': 1900,
        'itemName': "You Never Walk Alone",
    },
    {
        'imgURL': "../assets/BTSAlbums/18.jpg",
        'price': 1900,
        'itemName': "Love Yourself Tear",
    },
    ]
        results = []
        for product in btsAlbums:
            if query.lower() in product['itemName'].lower():
                results.append(product)
        return results

class BT21SearchAPIView(generics.ListAPIView):
    serializer_class = BTSMechSerializer
    def get_queryset(self):
        query = self.request.query_params.get('query', '')
        bt21 = [
    {
      'imgURL': "../assets/BT21Collection/1.jpg",
      'price': 1500,
      'itemName': "BT21 Soft Toys Mini",
    },
    {
      'imgURL': "../assets/BT21Collection/2.jpg",
      'price': 1800,
      'itemName': "BT21 Water Bottles",
    },
    {
      'imgURL': "../assets/BT21Collection/3.jpg",
      'price': 1200,
      'itemName': "BT21 Airpod Cover",
    },
    {
      'imgURL': "../assets/BT21Collection/4.jpg",
      'price': 1700,
      'itemName': "BT21 Slippers",
    },
    {
      'imgURL': "../assets/BT21Collection/5.jpg",
      'price': 1400,
      'itemName': "BT21 Socks",
    },
    {
      'imgURL': "../assets/BT21Collection/6.jpg",
      'price': 1900,
      'itemName': "BT21 Sleeping Mask",
    },
    {
      'imgURL': "../assets/BT21Collection/7.jpg",
      'price': 1100,
      'itemName': "BT21 Wrist Cushion",
    }]
        results = []
        for product in bt21:
            if query.lower() in product['itemName'].lower():
                results.append(product)
        return results



class ProducrSearchAPIView(generics.ListAPIView):
    serializer_class = BtsFashionSerializer
    def get_queryset(self):
        query = self.request.query_params.get('query', '')
        products = [
        {
        'imgURL': "../assets/BTSFashion/1.jpg",
        'price': 1500,
        'itemName': "Namjoon's Vogue Bottega Venetta Shirt",
        },
        {
        'imgURL': "../assets/BTSFashion/2.jpg",
        'price': 1800,
        'itemName': "Seokjin's Astronaut Interview Shirt",
        },
        {
        'imgURL': "../assets/BTSFashion/3.jpg",
        'price': 1200,
        'itemName': "Yoongi's Yet To Come Concert Shirt",
        },
        {
        'imgURL': "../assets/BTSFashion/4.jpg",
        'price': 1700,
        'itemName': "Jhope's The Dance Kid Shirt",
        },
        {
        'imgURL': "../assets/BTSFashion/5.jpg",
        'price': 1400,
        'itemName': "Jimin's Run BTS TShirt",
        },
        {
        'imgURL': "../assets/BTSFashion/6.jpg",
        'price': 1900,
        'itemName': "Taehyung's Spongebob-Fred Outfit",
        },
        {
        'imgURL': "../assets/BTSFashion/7.jpg",
        'price': 1100,
        'itemName': "Jungkook's OutFit on PTD LV Concert",
        },
        {
        'imgURL': "../assets/BTSFashion/8.jpg",
        'price': 1300,
        'itemName': "Namjoon's Balenciaga Black & White Shirt",
        },
        {
        'imgURL': "../assets/BTSFashion/9.jpg",
        'price': 1600,
        'itemName': "Jin's Pragmatic TShirt",
        },
        {
        'imgURL': "../assets/BTSFashion/10.jpg",
        'price': 2000,
        'itemName': "Yoongi's LV TShirt",
        },
        {
        'imgURL': "../assets/BTSFashion/11.jpg",
        'price': 1700,
        'itemName': "Hobi's Smiley Shirt",
        },
        {
        'imgURL': "../assets/BTSFashion/12.jpg",
        'price': 1500,
        'itemName': "Jimin's Dior Shirt",
        },
        {
        'imgURL': "../assets/BTSFashion/13.jpg",
        'price': 1800,
        'itemName': "Taehyung's Airport Fashion",
        },
        {
        'imgURL': "../assets/BTSFashion/14.jpg",
        'price': 1900,
        'itemName': "JK for CK",
        },
        {
      'imgURL': "../assets/BTSAlbums/1.jpg",
      'price': 1500,
      'itemName': "Proof Album",
        },
        {
        'imgURL': "../assets/BTSAlbums/2.jpg",
        'price': 1800,
        'itemName': "My Universe",
        },
        {
        'imgURL': "../assets/BTSAlbums/3.jpg",
        'price': 1200,
        'itemName': "Butter",
        },
        {
        'imgURL': "../assets/BTSAlbums/4.jpg",
        'price': 1700,
        'itemName': "BE",
        },
        {
        'imgURL': "../assets/BTSAlbums/5.jpg",
        'price': 1400,
        'itemName': "Skool Luv Affair",
        },
        {
        'imgURL': "../assets/BTSAlbums/6.jpg",
        'price': 1900,
        'itemName': "Love Yourself Answer",
        },
        {
        'imgURL': "../assets/BTSAlbums/7.jpg",
        'price': 1100,
        'itemName': "BTS World",
        },
        {
        'imgURL': "../assets/BTSAlbums/8.jpg",
        'price': 1300,
        'itemName': "Map Of The Soul Persona",
        },
        {
        'imgURL': "../assets/BTSAlbums/9.jpg",
        'price': 1600,
        'itemName': "Dark & Wild",
        },
        {
        'imgURL': "../assets/BTSAlbums/10.jpg",
        'price': 2000,
        'itemName': "2CoolForSkool",
        },
        {
        'imgURL': "../assets/BTSAlbums/11.jpg",
        'price': 1700,
        'itemName': "Skool Luv Affair",
        },
        {
        'imgURL': "../assets/BTSAlbums/12.jpg",
        'price': 1500,
        'itemName': "O!RUL82?",
        },
        {
        'imgURL': "../assets/BTSAlbums/13.jpg",
        'price': 1800,
        'itemName': "Most Beautiful Moment in Life",
        },
        {
        'imgURL': "../assets/BTSAlbums/14.jpg",
        'price': 1900,
        'itemName': "Young Forever",
        },
        {
            'imgURL': "../assets/BTSAlbums/15.jpg",
            'price': 1900,
            'itemName': "Love Yourself Her",
        },
        {
            'imgURL': "../assets/BTSAlbums/16.jpg",
            'price': 1900,
            'itemName': "Wings",
        },
        {
            'imgURL': "../assets/BTSAlbums/17.jpg",
            'price': 1900,
            'itemName': "You Never Walk Alone",
        },
        {
            'imgURL': "../assets/BTSAlbums/18.jpg",
            'price': 1900,
            'itemName': "Love Yourself Tear",
        },
        {
        'imgURL': "../assets/BT21Collection/1.jpg",
        'price': 1500,
        'itemName': "BT21 Soft Toys Mini",
        },
        {
        'imgURL': "../assets/BT21Collection/2.jpg",
        'price': 1800,
        'itemName': "BT21 Water Bottles",
        },
        {
        'imgURL': "../assets/BT21Collection/3.jpg",
        'price': 1200,
        'itemName': "BT21 Airpod Cover",
        },
        {
        'imgURL': "../assets/BT21Collection/4.jpg",
        'price': 1700,
        'itemName': "BT21 Slippers",
        },
        {
        'imgURL': "../assets/BT21Collection/5.jpg",
        'price': 1400,
        'itemName': "BT21 Socks",
        },
        {
        'imgURL': "../assets/BT21Collection/6.jpg",
        'price': 1900,
        'itemName': "BT21 Sleeping Mask",
        },
        {
        'imgURL': "../assets/BT21Collection/7.jpg",
        'price': 1100,
        'itemName': "BT21 Wrist Cushion",
        }
        ]
        results = []
        for product in products:
            if query.lower() in product['itemName'].lower():
                results.append(product)
        return results
