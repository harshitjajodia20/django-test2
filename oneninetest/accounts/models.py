from django.db import models

# Create your models here.
class Accounts(models.Model):
    servername = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return self.servername
