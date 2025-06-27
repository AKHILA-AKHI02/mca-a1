from django.db import models


# Create your models here.
class Member(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    phone=models.IntegerField(null=True)
    joined_date=models.DateField(null=True)
    
    def __str__(self):
        return self.firstname