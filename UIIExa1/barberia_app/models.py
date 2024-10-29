from django.db import models

# Create your models here.

class Local(models.Model):
    id_local=models.PositiveSmallIntegerField()
    direccon=models.CharField(max_length=100)
    color=models.CharField(max_length=100)
    telefono=models.CharField(max_length=10)
    trabajadores=models.PositiveSmallIntegerField()
    horarios=models.TimeField()
    ambiente=models.CharField(max_length=100)
    servicios=models.CharField(max_length=100)

    def __str__(self):
        return self.servicios