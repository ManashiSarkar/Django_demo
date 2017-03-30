from __future__ import unicode_literals
from django.utils import timezone

from django.db import models

# Create your models here.

class Comment(models.Model):
	author = models.ForeignKey('auth.user')
	post = models.ForeignKey('blog.Post')
	text = models.CharField(max_length=300,blank=False)
	created_date = models.DateTimeField(default=timezone.now)

	def __unicode__(self):
		return self.text
