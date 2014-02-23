from django.db import models
from testpage import settings




class User(models.Model):
	name = models.CharField(max_length=100)
	surname = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name

class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.CharField(max_length=100)
	user = models.ForeignKey(User)

	def __unicode__(self):
		return self.title