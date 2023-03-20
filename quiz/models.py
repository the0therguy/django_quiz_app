from django.db import models


# Create your models here.

class QuizCategory(models.Model):
    title = models.CharField(max_length=200)
    details = models.TextField()
    image = models.ImageField(upload_to='quiz_category_image/')

    def __str__(self):
        return self.title
