from django.urls import path
from .views import home, index, create_post
from blog import views

urlpatterns = [
    path('home', home),
    path('index', index),
    path('create_post', create_post),

    path('', views.home, name='home-url'),
    path('create_post/', views.create_post, name='create_post-url'),

]
