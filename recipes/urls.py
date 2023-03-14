from django.urls import path
from recipes.views import home,contato

urlpatterns = [
    path('', home),
    path('contato/', contato),
]
