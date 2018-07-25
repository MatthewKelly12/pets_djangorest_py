from django.shortcuts import render
from rest_framework import viewsets
from .models import Pets, Owners, Types
from .serializers import PetsSerializer, TypesSerializer, OwnersSerializer

class PetsView(viewsets.ModelViewSet):
    queryset = Pets.objects.all()
    serializer_class = PetsSerializer


class TypesView(viewsets.ModelViewSet):
    queryset = Types.objects.all()
    serializer_class = TypesSerializer


class OwnersView(viewsets.ModelViewSet):
    queryset = Owners.objects.all()
    serializer_class = OwnersSerializer


