from django.db import models


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=200)
    details = models.TextField()
    image = models.ImageField(upload_to='quiz_category_image/')

    def __str__(self):
        return self.title


class Question(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    question = models.TextField()
    option_1 = models.CharField(max_length=200)
    option_2 = models.CharField(max_length=200)
    option_3 = models.CharField(max_length=200)
    option_4 = models.CharField(max_length=200)
    difficulty = models.CharField(max_length=100)
    time_limit = models.IntegerField()
    answer = models.CharField(max_length=200)

    def __str__(self):
        return self.question


