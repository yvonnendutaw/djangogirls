from __future__ import unicode_literals

from django.db import models

from django.utils import timezone

#indicates that we are defining the model
#post is the name of the model
class Post(models.Model):
#author, title,text,createde_at, published_date are properties of the object
    author = models.ForeignKey("auth.User")
    title = models.CharField(max_length=150)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateField(blank = True, null = True)

    #this is the publish method 
    def publish(self):
        self.published_date =  timezone.now()
        self.save()

    def __str__(self):
        return self.title
