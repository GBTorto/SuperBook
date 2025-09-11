from django.urls import path
from . import views
from .views import PostList, PostCreateView

urlpatterns = [
    path('lista_posts/', views.lista_posts, name='lista_posts'),
    path('cbv-post/', PostList.as_view()),
    path('posts/novo/', PostCreateView.as_view(), name='novo_post'),
]

# Gabriel Morais