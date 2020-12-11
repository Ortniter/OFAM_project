from django.urls import path

from . import views

urlpatterns = [
    path('1270547075:AAHb_afunhhW2CWQrZ84NWYCbvHVz-AoYNk/', views.index, name='index'),
    path('update_shop/', views.update_shop, name='update_shop')
]