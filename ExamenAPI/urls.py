from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from vehiculos.views import VehiculoViewSet

router = DefaultRouter()
router.register(r'vehiculos', VehiculoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]