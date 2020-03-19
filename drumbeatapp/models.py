from django.db import models



class Instruments(models.Model):
    name = models.CharField(max_length=30)
    sound = models.CharField(max_length=2000)


    def __str__(self):
        return self.name