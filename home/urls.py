from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lost/', views.lost, name='lost'),
    path('found/', views.found, name='found'),
    path('about/', views.about, name='about'),
    path('lost_item/', views.lost_item, name='lost_item'),
    path('add_lost/', views.add_lost, name='add_lost'),
    path('add_found/', views.add_found, name='add_found'),
]