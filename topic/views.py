from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post
from .models import Topic

# Create your views here.

def topic_list(request):
	user = request.user

	if not Topic.objects.filter(label='computer_science'):
		Topic.objects.create(label='computer_science')

	if not Topic.objects.filter(label='backend_development'):
		Topic.objects.create(label='backend_development')

	if not Topic.objects.filter(label='mathematics'):
		Topic.objects.create(label='mathematics')

	if Topic.objects.filter(label='computer science'):
		Topic.objects.filter(label='computer science').delete()

	if Topic.objects.filter(label='backend development'):
		Topic.objects.filter(label='backend development').delete()

	topics = Topic.objects.all()
	
	topics.order_by('label')

	for topic in topics:
		print topic.label

	return render(request,'topic/topic_list.html',{'topics':topics})

def topic_detail(request,label):
	user = request.user

	topic = Topic.objects.get(label=label)

	posts = Post.objects.filter(topic=topic) #error, possibly wrong modelling, or wrong query

	return render(request,'topic/topic_detail.html',{'label':label,'posts':posts})













