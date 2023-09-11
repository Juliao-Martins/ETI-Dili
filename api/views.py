from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from eti.models import PerfilEscola, Galeri, Notisia, Autor, Categoria
from .serializers import NotisiaSerializer, UserSerializer, AutorSerializer, CategoriaSerializer

class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]

  

class AutorViewSet(viewsets.ModelViewSet):
  queryset = Autor.objects.all()
  serializer_class = AutorSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]



class NotisiaViewSet(viewsets.ModelViewSet):
  queryset = Notisia.objects.all()
  serializer_class = NotisiaSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CategoriaViewSet(viewsets.ModelViewSet):
  queryset = Categoria.objects.all()
  serializer_class = CategoriaSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]
