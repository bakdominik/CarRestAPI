import requests
import json

from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import Car, Rate
from .utils import make_exists, model_exists


class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    make = serializers.CharField(max_length=50)
    model = serializers.CharField(max_length=50)
    avg_rating = serializers.FloatField(required=False)

    def validate(self, data):
        make = data['make']
        model = data['model']

        # make validation using vpic API
        if make_exists(make):
            # model validation using vpic API
            if model_exists(make, model):
                return data
            else:
                raise serializers.ValidationError("The model does not exist.")
        else:
            raise serializers.ValidationError("The make does not exist.")

    def create(self, validated_data):
        return Car.objects.create(**validated_data)

    class Meta:

        validators = [
            UniqueTogetherValidator(
                queryset=Car.objects.all(),
                fields=['make', 'model']
            )
        ]


class PopularSerializer(serializers.ModelSerializer):
    rates_number = serializers.IntegerField()

    class Meta:
        model = Car
        fields = ('id', 'make', 'model', 'rates_number')


class RateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rate
        exclude = ['id']
