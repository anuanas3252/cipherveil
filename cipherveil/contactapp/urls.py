from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path('add_contact/', views.add_contact, name='add_contact'),
    path('view_contact/', views.view_contact, name='view_contact'),
    path('edit_contact/<int:pk>', views.edit_contact, name='edit_contact'),
    path('delete_contact/<int:pk>', views.delete_contact, name='delete_contact'),
]
