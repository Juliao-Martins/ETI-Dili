from django.db import models

import uuid


class PerfilEscola(models.Model):
  naran = models.CharField(max_length=150)
  enderesu = models.CharField(max_length=100)
  data_estabelece = models.DateField('Data estabelece')
  naran_director = models.CharField(max_length=255)
  img_director = models.ImageField(upload_to='perfil')
  liamenon_director = models.TextField()
  email = models.EmailField()
  youtube = models.URLField()
  facebook = models.URLField()
  nu_kontaktu = models.CharField(max_length=13)
  logo = models.ImageField(upload_to='perfil')
  historia = models.TextField()
  vizaun = models.TextField()
  misaun = models.TextField()
  objetivu = models.TextField()
  total_estudante = models.IntegerField(default=0)
  total_manorin = models.IntegerField(default=0)
  fasilidade = models.ManyToManyField('Fasilidade', blank=True)
  user = models.ForeignKey('auth.user', related_name='perfilescolas', on_delete=models.CASCADE)
  id = models.UUIDField(primary_key=True, editable=False, unique=True, default=uuid.uuid4)

  def __str__(self):
    return self.naran



class Fasilidade(models.Model):
  data_kria = models.DateTimeField(auto_now_add=True)
  data_modifika = models.DateTimeField(auto_now=True)
  naran = models.CharField(max_length=100)
  img = models.ImageField(upload_to='fasilidade')
  deskrisaun = models.TextField()
  id = models.UUIDField(primary_key=True, editable=False, unique=True, default=uuid.uuid4)

  def __str__(self):
    return self.naran



class Departamento(models.Model):
  data_kria = models.DateTimeField(auto_now_add=True)
  data_modifika = models.DateTimeField(auto_now=True)
  naran = models.CharField(max_length=100)
  img = models.ImageField(upload_to='departamento')
  deskrisaun = models.TextField()
  atividade_prinsipal = models.ManyToManyField('AtividadePrincipal', blank=True)
  programa_socio = models.ManyToManyField('ProgramaSocio', blank=True)
  programa_cientifico = models.ManyToManyField('ProgramaCientifico', blank=True)
  programa_produtivo = models.ManyToManyField('ProgramaProdutivo', blank=True)
  escola = models.ForeignKey(PerfilEscola, related_name='departamentos', on_delete=models.CASCADE)
  id = models.UUIDField(primary_key=True, editable=False, unique=True, default=uuid.uuid4)

  def __str__(self):
    return self.naran



class AtividadePrincipal(models.Model):
  programa = models.TextField()

  def __str__(self):
    return self.programa


class ProgramaSocio(models.Model):
  programa = models.TextField()

  def __str__(self):
    return self.programa


class ProgramaCientifico(models.Model):
  programa = models.TextField()

  def __str__(self):
    return self.programa

class ProgramaProdutivo(models.Model):
  programa = models.TextField()

  def __str__(self):
    return self.programa



class Autor(models.Model):
  naran = models.CharField(max_length=150)
  user = models.ForeignKey('auth.user', related_name='autors', on_delete=models.CASCADE)
  id = models.UUIDField(primary_key=True, editable=False, unique=True, default=uuid.uuid4)

  def __str__(self):
    return self.naran



class Notisia(models.Model):
  data_publikasaun = models.DateTimeField(auto_now_add=True)
  data_modifika = models.DateTimeField(auto_now=True)
  autor = models.ForeignKey(Autor, related_name='autors', on_delete=models.CASCADE)
  titulu = models.CharField(max_length=100)
  img = models.ImageField(upload_to='notisia')
  content = models.TextField()
  categoria = models.ManyToManyField('Categoria', blank=True)
  id = models.UUIDField(primary_key=True, editable=False, unique=True, default=uuid.uuid4)

  def __str__(self):
    return self.titulu



class Categoria(models.Model):
  naran = models.CharField(max_length=100)

  def __str__(self):
    return self.naran


class Galeri(models.Model):
  data_publikasaun = models.DateTimeField(auto_now_add=True)
  data_modifika = models.DateTimeField(auto_now=True)
  titulu = models.CharField(max_length=100)
  img = models.ImageField(upload_to='galeri')
  user = models.ForeignKey('auth.user', related_name='galeris', on_delete=models.CASCADE)
  id = models.UUIDField(primary_key=True, editable=False, unique=True, default=uuid.uuid4)

  def __str__(self):
    return self.titulu