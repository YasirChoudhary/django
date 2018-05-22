from django.db import models

class User(models.Model):
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=12)

    def __str__(self):
        return self.username

'''
class Details(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile_no = models.IntegerField()
    

'''
