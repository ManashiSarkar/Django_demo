from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm

# Create your views here.

def post_list(request):
	posts = Post.objects.all()
	return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request,pk):
	posts = Post.objects.filter(pk=pk)
	return render(request, 'blog/post_detail.html', {'posts': posts})

# requires login
def starred_post(request,pk):
	if request.user.is_authenticated:
		post = Post.objects.get(pk=pk)
		post.stars = post.stars+1
		post.save()
	return redirect('post_detail', pk=pk)

# requires login
def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
		else:
			return redirect('post_detail', pk=1000000000)
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form': form})

# requires login
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


