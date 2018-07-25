from django.urls import path, include
from .  import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('pets', views.PetsView)
router.register('types', views.TypesView)
router.register('owners', views.OwnersView)

urlpatterns = [
    path('', include(router.urls))
]