from django.db import models

# Create your models here.

class Msg(models.Model):
    name = models.CharField(max_length=50)
    mail = models.CharField(max_length=50)
    mob = models.CharField(max_length=15, default='0000000000')  
    msg = models.CharField(max_length=200)