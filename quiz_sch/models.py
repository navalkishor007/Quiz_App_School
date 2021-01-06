from django.db import models

# Create your models here.


class Question(models.Model):
    question = models.CharField(max_length=200)
    option_1 = models.CharField(max_length=20)
    option_2 = models.CharField(max_length=20)
    option_3 = models.CharField(max_length=20)
    option_4 = models.CharField(max_length=20)
    right_ans = models.CharField(max_length=20)

    def __str__(self):
        return self.question