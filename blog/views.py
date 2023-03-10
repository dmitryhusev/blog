from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post


class PostView(ListView):
    model = Post
    template_name = "home.html"


class BlogDetailView(DetailView):  # new
    model = Post
    template_name = "post_detail.html"


class BlogCreateView(CreateView): # new
    model = Post
    template_name = "post_new.html"
    fields = ["title", "author", "body"]