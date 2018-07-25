from rest_framework import serializers
from .models import Pets, Types, Owners

class PetsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pets
        fields = ('id', 'url', 'name', 'types')

class TypesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Types
        fields = ('id', 'url', 'name')

class OwnersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Owners
        fields = ('id', 'url', 'name', 'pets')