from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'events', views.EventViewSet)
router.register(r'exhibitions', views.ExhibitionViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
