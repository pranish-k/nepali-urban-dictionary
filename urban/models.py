from django.db import models

class Word(models.Model):
    title = models.CharField(max_length=200)
    meaning= models.CharField(max_length=1000)
    sentence = models.CharField(max_length=1000, null='True', blank='True')
    correct = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
