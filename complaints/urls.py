from django.urls import path
from . import views

app_name = 'complaints'

urlpatterns = [
    path('', views.complaint, name='complaint'),
    path('submit/', views.submit_complaint, name='submit_complaint'),
    path('check/', views.secy_complaint, name='secy_complaint'),
    path('delete/', views.delete, name='delete'),
    path('check/resolved/', views.resolved, name='resolved'),
]
