from rest_framework import serializers

from products.models import Product


from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def validate_code(self, value):
        if Product.objects.filter(code=value).exists():
            raise serializers.ValidationError("A product with this code already exists.")
        return value
