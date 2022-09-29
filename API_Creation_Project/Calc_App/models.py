from django.db import models


# Create your models here.
class api_creation_db(models.Model):

    request_time = models.CharField(max_length=50)
    ip_address = models.CharField(max_length=50)
    inputA = models.IntegerField()
    inputB = models.IntegerField()
    sum = models.IntegerField()
    subtraction = models.IntegerField()
    multiplication = models.IntegerField()
    division = models.FloatField()
