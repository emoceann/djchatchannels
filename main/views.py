from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy

# Create your views here.

#def home(request):
    #return render(request, 'home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-article_date']

class ArticleViews(DetailView):
    model = Post
    template_name = 'article.html'

class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post.html'

class EditView(UpdateView):
    model = Post
    template_name = 'edit_post.html'
    form_class = PostForm
    # fields = ['title', 'title_tag', 'body']

class DeleteArticle(DeleteView):
    model = Post
    template_name = 'delete_article.html'
    success_url = reverse_lazy('home')

