from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phno = models.IntegerField()
    desc = models.TextField()
    city = models.CharField(max_length=30)
    zipcode = models.IntegerField()
