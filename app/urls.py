from django.urls import path
from . import views

urlpatterns = [
    path( '',views.index,name='index',),
    path('hello', views.hello, name='hello'),
    path('users', views.users, name='users'),
    path('new_users', views.new_users, name='new_users'),
    path('info_users/<int:id>', views.info_users, name='info_users'),  
]

