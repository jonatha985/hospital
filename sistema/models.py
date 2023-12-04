from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.
class Doutor(models.Model):
    name = models.CharField(null=False, blank=False,max_length=50)
    username = models.CharField(null=False, blank=False,max_length=50)
    password = models.CharField(null=False, blank=False,max_length=50)
    crm = models.IntegerField(null=False, blank=False)
    email = models.CharField(null=False, blank=False,max_length=50)
    especialidade = models.CharField(null=False, blank=False,max_length=50)

    def __str__(self):
        return self.name

class Recepcionista(models.Model):
    name = models.CharField(null=False, blank=False,max_length=50)
    username = models.CharField(null=False, blank=False,max_length=50)
    password = models.CharField(null=False, blank=False,max_length=50)
    email = models.CharField(null=False, blank=False,max_length=50)
    turno = models.CharField(null=False, blank=False,max_length=50)

    def __str__(self):
        return self.name
