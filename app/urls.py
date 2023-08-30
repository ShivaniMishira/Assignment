from django.urls import path
from . import views

urlpatterns = [
    path( '',views.index,name='index',),
    path('hello', views.hello, name='hello'),
    path('users', views.users, name='users'),
    path('new_users', views.new_users, name='new_users'),
    path('info_users/<int:id>', views.info_users, name='info_users'),  
    path('update/<int:id>', views.update, name='update'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('search', views.search, name='search'),

]

