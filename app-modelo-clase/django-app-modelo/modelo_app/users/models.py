from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    profile_image = models.URLField()  

    def __str__(self):
        return self.name
