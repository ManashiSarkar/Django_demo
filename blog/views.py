from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post
from userinfo.models import PostInfo
from .forms import PostForm

# Create your views here.

def post_list(request):
	posts = Post.objects.all()
	return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request,pk):
	try:
		post = get_object_or_404(Post, pk=pk)
	except:
		return render( request, 'home/doesnotexist.html', {} )

	user = request.user

	if user.is_authenticated:
		try:
			postinfo = PostInfo.objects.filter(user=user).get(post=post)
		except:
			PostInfo.objects.create(user=user,post=post)
			postinfo = PostInfo.objects.filter(user=user).get(post=post)
		
		context = {'post': post,'postinfo': postinfo}

		#print post.user + ' ' + request.user

	else:
		context = {'post': post,'postinfo': None}

	return render(request, 'blog/post_detail.html', context)

# requires login
def starred_post(request,pk):
	user = request.user
	if user.is_authenticated and Post.objects.filter(pk=pk):
		post = Post.objects.get(pk=pk)
		'''
		if not PostInfo.objects.filter(user=user):
			PostInfo.objects.create(user=user,post=post)

		elif not PostInfo.objects.filter(user=user).filter(post=post):
			PostInfo.objects.create(user=user,post=post)
		'''
		post_info = PostInfo.objects.filter(user=user).get(post=post)
		post_info.toggle(post)

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
			return render( request, 'home/invalidform.html', {} )
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

def post_publish(request,pk):
	user = request.user

	try:
		post = get_object_or_404(Post, pk=pk)
	except:
		return render(request, 'home/invalidurl.html', {})

	if user.is_authenticated:
		if user == post.author:
			post.publish()

	return redirect('user_detail', username=post.author.username)

def post_unpublish(request,pk):
	user = request.user

	try:
		post = get_object_or_404(Post, pk=pk)
	except:
		return render(request, 'home/invalidurl.html', {})

	if user.is_authenticated:
		if user == post.author:
			post.unpublish()

	return redirect('user_detail', username=post.author.username)

def post_delete(request,pk):
	user = request.user

	try:
		post = get_object_or_404(Post, pk=pk)
	except:
		return render(request, 'home/invalidurl.html', {})

	if user.is_authenticated:
		if user == post.author:
			post.delete()

	return redirect('user_detail', username=post.author.username)