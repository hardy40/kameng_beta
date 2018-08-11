from django.urls import path
from . import views

app_name = 'facility'

urlpatterns = [
    path('', views.facility, name='facility'),
]
