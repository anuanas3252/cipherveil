from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path('steganoencode/', views.steganoencode, name='steganoencode'),
    path('steganodecode/', views.steganodecode, name='steganodecode'),
    
   path('download_image/<str:image_name>/', views.download_image_view, name='download_image'),

]
