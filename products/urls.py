from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('seafood', views.seafood),
    path('fruits', views.fruit),
    path('veg', views.veg)
]
