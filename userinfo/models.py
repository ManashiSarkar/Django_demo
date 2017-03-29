from __future__ import unicode_literals

from django.db import models

# Create your models here.

class PostInfo(models.Model):
	user = models.ForeignKey('auth.User')
	post = models.ForeignKey('blog.Post')
	isfavorite = models.BooleanField(default=False)

	def toggle(self,post):
		if not self.isfavorite:
			post.stars = post.stars + 1
		else:
			post.stars = post.stars - 1
		self.isfavorite = not self.isfavorite
		self.save()
		post.save()

	def __unicode__(self):
		return self.post.title
