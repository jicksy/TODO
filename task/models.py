from django.db import models
from django.contrib.auth.models import User
from project.models import Project

# Create your models here.
class Task(models.Model):
	PRIORITY_LIST=[('1',"High"),('2',"Medium"),('3',"Low"),]

	name=models.CharField(max_length=20)
	description=models.CharField(max_length=200)
	start=models.DateField()
	end=models.DateField()
	priority=models.CharField(
		max_length=1,
		choices=PRIORITY_LIST)
	project=models.ForeignKey(Project)
	user=models.ForeignKey(User)
	

	def __unicode__(self):
		return self.name +":" + self.priority
