from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path('encryptionkeygenerate/', views.encryptionkeygenerate, name='encryptionkeygenerate'),
    path('decryptionkeygenerate/', views.decryptionkeygenerate, name='decryptionkeygenerate'),
    path('messageencrypt/', views.messageencrypt, name='messageencrypt'),
    path('messagedecrypt/', views.messagedecrypt, name='messagedecrypt'),
]
