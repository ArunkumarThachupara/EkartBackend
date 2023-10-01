from rest_framework import serializers
from .models import BtsFashion, BtsAlbum, BT21

class BTSMechSerializer(serializers.Serializer):
    imgURL = serializers.CharField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    itemName = serializers.CharField()


class BtsFashionSerializer(serializers.Serializer):
    imgURL = serializers.CharField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    itemName = serializers.CharField()


class BtsAlbumSerializer(serializers.ModelSerializer):
    imgURL = serializers.CharField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    itemName = serializers.CharField()

class BT21Serializer(serializers.ModelSerializer):
    imgURL = serializers.CharField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    itemName = serializers.CharField()
