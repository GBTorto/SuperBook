from django.urls import path
from . import views
from .views import PostList, PostCreateView

urlpatterns = [
    path('lista/', PostList.as_view()),
    path('novo/', PostCreateView.as_view(), name='novo_post'),
]

# Gabriel Morais