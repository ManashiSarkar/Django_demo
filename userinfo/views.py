from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from blog.models import Post
from follow.models import Follow

# Create your views here.

def user_detail(request,username=None):
	if not request.user.is_authenticated and not username:
		return redirect('post_list')
	if not username:
		username = request.user.username
		return redirect('user_detail', username=username)
	try:
		user = get_object_or_404(User, username=username)
	except:
		print username
		return render( request, 'home/doesnotexist.html', {} )
		#return redirect('doesnotexist',pk=0) #error

	posts = Post.objects.filter(author=user)

	if request.user.is_authenticated:	
		try:
			follow = Follow.objects.get(person=request.user,following=user)
		except:
			Follow.objects.create(person=request.user,following=user)
			follow = Follow.objects.get(person=request.user,following=user)

		context = {'user':user,'posts':posts,'following':follow}
	else:
		context = {'user':user,'posts':posts,'following':None}
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
	
def user_follow(request,username=None):
	user = request.user

	if not user.is_authenticated:
		return redirect('user_detail', username=username)

	try:
		followee = get_object_or_404(User,username=username)
	except:
		return render( request, 'home/doesnotexist.html', {} )

	if user == followee:
		return render( request, 'home/invalidurl.html', {} )

	else:
		try:
			follow = Follow.objects.get(person=user,following=followee)
		except:
			Follow.objects.create(person=user,following=followee)
			follow = Follow.objects.get(person=user,following=followee)
		
		follow.isfollowing = True
		follow.save()

	return redirect('user_detail', username=username)

def user_unfollow(request,username=None):
	user = request.user

	if not user.is_authenticated:
		return redirect('user_detail', username=username)

	try:
		followee = get_object_or_404(User,username=username)
	except:
		return render( request, 'home/doesnotexist.html', {} )

	if user == followee:
		return render( request, 'home/invalidurl.html', {} )

	else:
		follow = Follow.objects.get(person=user,following=followee)
		follow.isfollowing = False
		follow.save()

	return redirect('user_detail', username=username)















