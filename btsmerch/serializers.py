from rest_framework import serializers
from .models import BtsFashion, BtsAlbum, BT21

class BtsFashionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BtsFashion
        fields = '__all__'

class BtsAlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = BtsAlbum
        fields = '__all__'

class BT21Serializer(serializers.ModelSerializer):
    class Meta:
        model = BT21
        fields = '__all__'
