from django.shortcuts import render, redirect
from .models import Post
from django.views.generic import ListView, CreateView
from .forms import PostForm
from django.urls import reverse_lazy

# Create your views here.
class PostList(ListView):
    model = Post
    template_name = "posts/lista_posts.html"
    context_object_name = "posts"

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/form_post.html'
    success_url = reverse_lazy('listar_posts')

# Gabriel Morais