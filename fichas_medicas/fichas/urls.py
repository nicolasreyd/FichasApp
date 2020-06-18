from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.fichas_form),
    path('list/',views.fichas_list)
]