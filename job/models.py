from django.db import models

# Create your models here.

'''
django model field:
    - html widget 
    - validation like E-mail
    - database size 

'''
class Job(models.Model):    # table in Database
    JOB_TYPE = [
        ('PT','Part Time') , 
        ('FT','Full Time'),]
    title = models.CharField(max_length = 100 , null=True , help_text='Enter Name Job')  # column in table
    #location = 
    job_type = models.CharField(max_length = 20,choices=JOB_TYPE , help_text='Enter Type of time in this job')
    description = models.TextField(null=True , help_text='Enter Description of Job' , max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(null=True,default=1)
    salary = models.IntegerField(default=0,null=True)
    experience = models.IntegerField(default=1,null=True) 
    
    def __str__(self):
        return self.title
    
    