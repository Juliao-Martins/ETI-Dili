from django.urls import path
from django.views.generic import TemplateView
from .views import VerandaTemplateView, PerfilTemplateView, NotisiaTemplateView, NotisiaDetailView, GaleriListView, DepartamentoDetailView, SeidaukTemplateView


app_name = 'eti'
urlpatterns = [
  path('', VerandaTemplateView.as_view(), name='veranda'),
  path('perfil/', PerfilTemplateView.as_view(), name='perfil'),
  path('vizaun-no-misaun/', PerfilTemplateView.as_view(template_name='eti/vizaun-no-misaun.html'), name='vizaun'),
  path('notisia/', NotisiaTemplateView.as_view(), name='notisia'),
  path('notisia/<slug:pk>/', NotisiaDetailView.as_view(), name='notisia-detail'),
  path('galeri/', GaleriListView.as_view(), name='galeri'),
  path('departamento/<slug:pk>/', DepartamentoDetailView.as_view(), name='departamento'),
  path('seidauk/', SeidaukTemplateView.as_view(template_name='eti/dadus-mamuk.html'), name='seidauk'),
  path('informasaun-inskrisaun/', SeidaukTemplateView.as_view(template_name='eti/informasaun-inskrisaun.html'), name='informasaun-inskrisaun'),
]