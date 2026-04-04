from decimal import Decimal
from store.models import Product, Collection
from rest_framework import serializers


class CollectionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=10, decimal_places=2, source='unit_price')
    # here we dont need match the field names with the model fields, we can use any name we want. but we need to specify the source of the data.
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    collection = CollectionSerializer()

    def calculate_tax(self, product: Product):
        taxed_price = round(product.unit_price * Decimal(1.1), 2)
        return taxed_price