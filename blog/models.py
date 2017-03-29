from __future__ import unicode_literals
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    stars = models.IntegerField(blank=True, default=0)
    ispublished = models.BooleanField(default=False)
    isdeleted = models.BooleanField(default=False)

    def publish(self):
        self.published_date = timezone.now()
        self.isdeleted = False
        self.ispublished = True
        self.save()

    def unpublish(self):
        #self.published_date = timezone.now()
        self.isdeleted = False
        self.ispublished = False
        self.save()

    def delete(self):
        self.published_date = timezone.now()
        self.ispublished = False
        self.isdeleted = True
        self.save()

    def __unicode__(self):
        return self.title
