from django.db import models
from datetime import datetime
# Create your models here.

class BlogImage(models.Model):
    name = models.CharField(max_length=128, null=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    def __strt__(self):
        return name
    def imageURL(self):
        try:
            url = self.image.url  
        except:
            url = ''
        return url

class Project(models.Model):
    name = models.CharField(max_length=144, null=False)
    shortdescription = models.CharField(max_length=1024, null=True)
    description = models.CharField(max_length=2048*4, null=True)
    URL = models.CharField(max_length=1024, null=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    blogimages = models.ManyToManyField(BlogImage)
    def __str__(self):
        return self.name
    @property
    def imageURL(self):
        try:
            url =  self.image.url
        except:
            url = ''
        return url
    
    
class CSTag(models.Model):
    name = models.CharField(max_length=144, null=False)
    Projects = models.ManyToManyField(Project)
    is_front_end = models.BooleanField(default=False, null=True)
    def __str__(self):
        return str(self.name)
    
    
class Prospect(models.Model):
    name = models.CharField(max_length=144, null=False)
    email = models.CharField(max_length=1024, null=False)
    message = models.CharField(max_length=2048*4, null=True)
    company = models.CharField(max_length=144, null=False, default='none')
    def __str__(self):
        return self.name
        
class WorkExperience(models.Model):
    company = models.CharField(max_length=144, null=False)
    title = models.CharField(max_length=144, null=False)
    
    start_year = models.DateField(default=datetime(1900,1,1))
    end_year = models.DateField(default=datetime(1900,1,1))
    is_current = models.BooleanField(default=False)
    
    def __str__(self):
        return self.company; 
        
class WorkSkill(models.Model):
    name = models.CharField(max_length=1024, null=False, blank=False, default='Skill')
    job = models.ForeignKey('WorkExperience', on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.name
