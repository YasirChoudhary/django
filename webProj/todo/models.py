from django.db import models



class User(models.Model):
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=12)

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_text = models.CharField(max_length=250)
    due_date = models.DateField()

    def __str__(self):
        return "{} , {}".format(self.task_text,self.due_date)



