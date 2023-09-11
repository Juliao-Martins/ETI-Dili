from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import UserViewSet, AutorViewSet, NotisiaViewSet, CategoriaViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'autors', AutorViewSet, basename='autor')
router.register(r'notisias', NotisiaViewSet, basename='notisia')
router.register(r'categorias', CategoriaViewSet, basename='categoria')


urlpatterns = [
  path('', include(router.urls))
]

urlpatterns += [
  path('api-auth/', include('rest_framework.urls'))
]