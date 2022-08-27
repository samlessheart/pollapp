from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Poll(models.Model):
    question = models.CharField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    count_1 = models.IntegerField(default=0)
    count_2 = models.IntegerField(default=0)
    count_3 = models.IntegerField(default=0)
    count_4 = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.question


class Answers(models.Model):
    option_1 = models.CharField(max_length=100)
    option_2 = models.CharField(max_length=100)
    option_3 = models.CharField(max_length=100)
    option_4 = models.CharField(max_length=100)
    question = models.OneToOneField(Poll, on_delete=models.CASCADE)



class Profile(models.Model):
    user = models.OneToOneField(User,  on_delete=models.CASCADE)
    que_counts = models.IntegerField(default=0)




