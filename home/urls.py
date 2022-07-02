from django.urls import path, include
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', include('allauth.urls')),
    path('lost/', views.lost, name='lost'),
    path('found/', views.found, name='found'),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('about/', views.about, name='about'),
    path('lost_item/', views.lost_item, name='lost_item'),
    path('add_lost/', views.add_lost, name='add_lost'),
    path('add_found/', views.add_found, name='add_found'),
    path('user_lost/', views.user_lost, name='user_lost'),
    path('user_found/', views.user_found, name='user_found'),
    path('edit_lost/<item_id>', views.edit_lost, name='edit_lost'),
    path('edit_found/<item_id>', views.edit_found, name='edit_found'),
    path('delete_lost/<item_id>', views.delete_lost, name='delete_lost'),
    path('delete_found/<item_id>', views.delete_found, name='delete_found'),
    path('search/', views.search, name='search'),
]