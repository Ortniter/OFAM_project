from django.urls import path

from . import views

urlpatterns = [
    path('1207325258:AAHnQUKZH82bX8IWrcG2UGrV43JNprOZEYA/', views.index, name='index'),
    path('update_shop/', views.update_shop, name='update_shop')
]