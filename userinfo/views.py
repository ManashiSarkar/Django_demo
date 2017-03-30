from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from blog.models import Post

# Create your views here.

def user_detail(request,username=None):
	if not request.user.is_authenticated and not username:
		return redirect('post_list')
	if not username:
		username = request.user.username
		return redirect('user_detail', username=username)
	print 'lol'
	try:
		user = get_object_or_404(User, username=username)
	except:
		print username
		return render( request, 'home/doesnotexist.html', {} )
		#return redirect('doesnotexist',pk=0) #error

	print 'after user'
	posts = Post.objects.filter(author=user)
	print 'after posts'
	context = {'user':user,'posts':posts}
	template = 'userinfo/profile.html'
	return render( request, template, context )

def user_bin(request,username=None):
	user = request.user
	if not user.is_authenticated:
		return redirect('user_detail', username=username)
	if user.username != username:
		return redirect('user_detail', username=username)

	posts = Post.objects.filter(author=user) #.filter(isdeleted=True)
	context = {'user':user,'posts':posts}
	template = 'userinfo/bin.html'
	return render( request, template, context )
	

