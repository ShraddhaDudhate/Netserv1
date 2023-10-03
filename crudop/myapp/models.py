from django.db import models



class Member(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    
    class Meta:
        app_label = 'myapp'
# Create your models here.
