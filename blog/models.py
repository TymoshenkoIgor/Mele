from django.db import models
from django.utils import timezone 
from django.contrib import User 


class Post(models.Model):
	STATUS_CHOICE = (
			('draft', 'Draft'),
			('published', 'Published'),
		)
	title = models.CharField(max_length=250)
	slug = models.SlugField(max_length=250, unique_for_date='publish')
	author = models.ForeignKey(User, related_name='blog_posts')
	body = models.TextField()
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	