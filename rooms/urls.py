from django.urls import path
from . import views

app_name = 'rooms'

urlpatterns = [
    path('', views.rooms, name='rooms'),
    #path('/<int:rollnum>', views.roll, name='Roll'),
]
