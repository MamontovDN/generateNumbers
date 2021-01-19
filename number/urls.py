from django.urls import path

from number import views

urlpatterns = [
    path('', views.index, name='index'),

]