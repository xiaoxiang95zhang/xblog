from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class BlogArticles(models.Model):
    title = models.CharField(max_length=300)
    auth = models.ForeignKey(User, related_name='blog_posters')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-publish',)
        db_table = 'articles'

    def __str__(self):
        return self.title


# Create your models here.
