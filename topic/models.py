from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Topic(models.Model):
	label = models.CharField(max_length=25)
	#posts = models.ManyToManyField('blog.Post',related_name='topic_posts')

	def add(self,label):
		if not Table.objects.filter(label=label):
			Table.objects.create(label=label)

	def remove(self,label):
		if Table.objects.filter(label=label):
			Table.objects.filter(label=label).delete()

	def __unicode__(self):
		return self.label

