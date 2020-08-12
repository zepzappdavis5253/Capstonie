from django.db import models
from django.contrib.auth.models import User



class Instrument(models.Model):
    name = models.CharField(max_length=30)
    sound = models.CharField(max_length=2000)


    def __str__(self):
        return self.name




class Score(models.Model):
    name = models.CharField(max_length=30)
    score_data = models.TextField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)


    def __str__(self):
        return self.name