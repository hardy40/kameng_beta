from django.urls import path
from . import views

app_name = 'event'

urlpatterns = [
    path('', views.posts, name='posts'),
    path('add/', views.add, name='add'),
]
