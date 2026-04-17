from django.db import models

# Create your models here.

class exampleModel(models.Model):
    name=models.CharField(max_length=100)
    age=models.FloatField()


    def __str__(self):
        return self.name