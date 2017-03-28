from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from blog.models import Post

# Create your views here.

def user_detail(request,username):
	user = get_object_or_404(User, username=username)
	posts = Post.objects.filter(author=user)
	context = {'user':user,'posts':posts}
	template = 'userinfo/profile.html'
	return render( request, template, context )
	

