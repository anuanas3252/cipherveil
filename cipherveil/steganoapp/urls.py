from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path('encrypt/', views.encrypt, name='encrypt'),
    path('decrypt/', views.decrypt, name='decrypt'),
    
   path('download_image/<str:image_name>/', views.download_image_view, name='download_image'),

]
