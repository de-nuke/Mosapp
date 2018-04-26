from rest_framework import serializers
from .models import MainImage


class MainImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = MainImage
        fields = ('photo', 'pk', )