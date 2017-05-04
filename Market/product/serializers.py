from .models import Product, Collection
from rest_framework import serializers


class CollectionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:

        model = Collection
        fields = ('url', 'category', 'product',)


class ProductSerializer(serializers.HyperlinkedModelSerializer):

    #Product = ProductSerializer()

    class Meta:

        model = Product
        fields = ('url', 'title', 'description', 'size', 'price', 'sale_price', 'photo')