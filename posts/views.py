from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
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

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/form_post.html'
    success_url = reverse_lazy('lista_posts')

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/confirmar_exclusao.html'
    success_url = reverse_lazy('lista_posts')

# class PostDetailView():


# Gabriel Morais