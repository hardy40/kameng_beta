from django.urls import path
from . import views

app_name = 'mess_menu'

urlpatterns = [
    path('', views.mess_response, name='mess_response'),
    path('submitted/', views.submitted, name='submitted'),
    path('vote/', views.vote, name='vote'),
    path('submitted/vote/',views.vote,name='vote2')
]
