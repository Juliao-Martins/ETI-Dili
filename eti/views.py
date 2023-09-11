from django.views.generic import DetailView, ListView, TemplateView
from .models import PerfilEscola, Galeri, Notisia, Autor, Departamento


class VerandaTemplateView(TemplateView):
  template_name = 'eti/veranda.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['perfil'] = PerfilEscola.objects.first()
    context['departamentus'] = Departamento.objects.all()
    context['departamentu_kolekta'] = Departamento.objects.order_by('data_kria')[:4]
    context["notisias"] = Notisia.objects.order_by('-data_publikasaun')[:3]
    context["footer"] = True
    return context


class PerfilTemplateView(TemplateView):
  template_name = 'eti/perfil.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['perfil'] = PerfilEscola.objects.first()
    context['departamentus'] = Departamento.objects.all()
    return context


class NotisiaTemplateView(TemplateView):
  template_name = 'eti/notisia.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['departamentus'] = Departamento.objects.all()
    return context


class NotisiaDetailView(DetailView):
  context_object_name = 'notisia'
  model = Notisia
  template_name='eti/notisia-detail.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['departamentus'] = Departamento.objects.all()
    context["notisia_relevante"] = Notisia.objects.all()[:4]
    return context


class GaleriListView(ListView):
  context_object_name = 'galeri'
  model = Galeri
  paginate_by = 5
  template_name = 'eti/galeri.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['departamentus'] = Departamento.objects.all()
    return context


class DepartamentoDetailView(DetailView):
  context_object_name = 'departamento'
  model = Departamento
  template_name = 'eti/departamentu.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['departamentus'] = Departamento.objects.all()
    return context


class SeidaukTemplateView(TemplateView):
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['departamentus'] = Departamento.objects.all()
    return context