from django.urls import path
from . import views
from .views import PostList

urlpatterns = [
    path('lista_posts/', views.lista_posts, name='lista_posts'),
    path('cbv-post/', PostList.as_view()),
    path('post_form/', views.criar_post, name='post_form'),
]

# Gabriel Morais