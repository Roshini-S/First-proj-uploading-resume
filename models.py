from django.db import models

# Create your models here.
class Studentdata(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    regno=models.IntegerField(max_length=20)
    college=models.CharField(max_length=20)
    mailid=models.EmailField(max_length=20)
    dept=models.CharField(max_length=20)
    skills=models.CharField(max_length=50)
    pincode=models.IntegerField(max_length=6)
    state=models.CharField(max_length=30)
    country=models.CharField(max_length=20)
class Meta:
    db_table="Studentdata"

