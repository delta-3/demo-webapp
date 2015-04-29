from django.db import models

class User(models.Model):
	username = models.CharField(max_length=35)
	password = models.CharField(max_length=200)
	firstname = models.CharField(max_length=35)
	lastname = models.CharField(max_length=35)
	age = models.CharField(max_length=3)

	def __unicode__(self):
		return "username :" + str(self.username) + ", password : " + str(self.password)

class Gif(models.Model):
	gif_name = models.CharField(max_length=20)
	gif_url = models.URLField(max_length=200)

	def __unicode__(self):
		return "gif_name :" + str(self.gif_name) + ", gif_url : " + str(self.gif_url)
		
class Comment(models.Model):
	#user = models.ForeignKey(User)
	content = models.CharField(max_length=200)

	def __unicode__(self):
		#return "user :" + str(self.user) + ", content : " + str(self.content)
		return "content : " + str(self.content)
