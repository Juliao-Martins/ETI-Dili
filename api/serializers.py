from django.contrib.auth.models import User
from rest_framework import serializers
from eti.models import Autor, Notisia, Categoria



class UserSerializer(serializers.HyperlinkedModelSerializer):

  autors = serializers.HyperlinkedRelatedField(queryset=Autor.objects.all(), many=True, view_name='autor-detail')
  
  class Meta:
    model = User
    fields = ['url', 'username', 'email', 'autors']



class AutorSerializer(serializers.HyperlinkedModelSerializer):

  user = serializers.ReadOnlyField(source='user.username')
  notisias = serializers.HyperlinkedRelatedField(queryset=Notisia.objects.all(), view_name='notisia-detail', many=True)

  class Meta:
    model = Autor
    fields = ['url', 'naran', 'user', 'notisias']



class NotisiaSerializer(serializers.HyperlinkedModelSerializer):
  
  autor = serializers.ReadOnlyField(source='autor.naran')

  class Meta:
    model = Notisia
    fields = ['url', 'id', 'data_publikasaun', 'titulu', 'img', 'content', 'categoria', 'autor']



class CategoriaSerializer(serializers.HyperlinkedModelSerializer):

  class Meta:
    model = Categoria
    fields = ['url', 'naran']