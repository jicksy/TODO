from django.db import models
from django.contrib.auth.models import User,Group
# Create your models here.
import datetime

from django.utils import timezone

class Project(models.Model):
	project_name=models.CharField(max_length=200)
	project_desc=models.TextField(null=True)
	start_date=models.DateField()
	end_date=models.DateField()
	#user=models.ForeignKey(User)


	
	user=models.ForeignKey(User)
	groups=models.ManyToManyField(Group)


	

