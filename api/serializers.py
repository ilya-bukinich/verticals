from rest_framework import serializers
from bbs.models import Advert, Category


class AdvertListSerializer(serializers.ModelSerializer):
    """
    Serialize the list of ads
    """
    class Meta:
        model = Advert
        fields = ['title', 'image', 'price', 'create_datetime']


class AdvertSerializer(serializers.ModelSerializer):
    """
    Serialize ad
    """
    class Meta:
        model = Advert
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    """
    Serialize the list of categories
    """
    class Meta:
        model = Category
        fields = '__all__'
