from django.db import models

# Create your models here.
class MyApiModel(models.Model):
    eid=models.IntegerField()
    name=models.CharField(max_length=50)
    class1=models.CharField(max_length=20)
    email=models.EmailField(max_length=80)

    def __str__(self):
        return self.name
    

