from django.shortcuts import render
from .models import Post
from django.views import generic

# Create your views here.

class BlogView(generic.DetailView):
    model = Post
    template_name = 'blog.html'

#Template view is used when user needs to render data without a a model
class AboutView(generic.TemplateView):
    #note! this view does not come derived from a model
    template_name = 'about.html'

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('date_created')
    template_name = 'index.html'