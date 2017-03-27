from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request,pk):
	posts = Post.objects.filter(pk=pk)
	return render(request, 'blog/post_detail.html', {'posts': posts})
