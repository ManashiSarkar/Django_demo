from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Follow(models.Model):
	person = models.ForeignKey('auth.User')
	following = models.ForeignKey('auth.User',related_name='followee')
	isfollowing = models.BooleanField(default=False)

	def follow(self):
		pass

	def __unicode__(self):
		return self.follower.username + ' -> ' + self.person.username
