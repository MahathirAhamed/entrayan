from django.db import models
from django.contrib.auth.models import User
import json


class CourseInfo(models.Model):
    course_name = models.CharField(max_length=200, null=False)
    course_description = models.CharField(max_length=200, null=False)
    course_duration = models.TimeField(auto_now_add=True, null=False)
    course_date = models.DateTimeField(null=False)
    author_name = models.CharField(max_length=200, null=False)
    author = models.ForeignKey(User)
    created_date = models.DateTimeField(auto_now_add=True, null=False)
    def as_dict(self): 
        return dict(course_id=self,
                    course_name=self.course_name,
                    course_duration=self.course_duration,
                    course_date=self.course_date,
                    author_name=self.author_name,
                    author_id=self.author,
                    created_date=self.created_date)
    

class SubscriberInfo(models.Model):
    course_subscribed = models.CharField(max_length=200, null=False)
    course = models.ForeignKey(CourseInfo)
    subscriber = models.ForeignKey(User)
    course_date = models.DateTimeField(null=False)
    subscribed_date = models.DateTimeField(auto_now_add=True, null=False)


class AlertInfo(models.Model):
    alert_type = models.CharField(max_length=50, null=False)
    alert_status = models.CharField(max_length=50, null=False)
    alert_for = models.CharField(max_length=100, null=False)
    sent_to = models.ForeignKey(User)
    sent_date = models.DateTimeField(auto_now=True, null=False)
    
     


    

