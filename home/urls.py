from django.urls import path

from . import views

app_name = 'home'

urlpatterns = [
    path('',views.home,name="home"),
    path('whatsapp',views.whatsapp,name="whatsapp"),
    path('seguro', views.seguro, name="seguro"),
    path('credito', views.credito, name="credito"),
]