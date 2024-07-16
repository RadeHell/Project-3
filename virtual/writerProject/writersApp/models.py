from django.db import models

class Order(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  adress = models.CharField(max_length=255)

def __str__(self):
    return f"{self.firstname} {self.lastname}"