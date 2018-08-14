from django.urls import path
from . import views

app_name = 'rooms'

urlpatterns = [
    path('', views.rooms, name='rooms'),
    path('search/', views.roll, name='roll'),
    path('add/', views.add_kamengite, name='add'),
]
