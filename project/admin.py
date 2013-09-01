from django.contrib import admin
from project.models import Project
from task.models import Task
from django.contrib.auth.models import User

class TaskInLine(admin.TabularInline):
	model=Task
	extra=3


class ProjectAdd(admin.ModelAdmin):
	fieldsets=[
	(None,{'fields':['project_name','user']}),
	('Project Desciption',{ 'fields':['project_desc'] ,'classes':['collapse'], }),
	('Dates to Note',{'fields':['start_date','end_date'] }),
	]
	inlines = [TaskInLine]
	
	


admin.site.register(Project,ProjectAdd)

