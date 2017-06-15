from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
@python_2_unicode_compatible
class Map(models.Model):        
    title = models.CharField(max_length=200)
    post = models.CharField(max_length=200)
    user = models.ForeignKey(User)
    longitude = models.FloatField(default = 0)
    latitude = models.FloatField(default= 0)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)


    def __str__(self):
        return self.title