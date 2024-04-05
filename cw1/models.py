from django.db import models

class Story(models.Model):
    unique_key = models.AutoField(primary_key=True)
    headline = models.CharField(max_length=64)
    CATEGORY_CHOICES = [
        ('pol', 'Politics'),
        ('art', 'Art'),
        ('tech', 'Technology'),
        ('trivia', 'Trivia')
    ]
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    REGION_CHOICES = [
        ('uk', 'UK'),
        ('eu', 'EU'),
        ('w', 'World')
    ]
    region = models.CharField(max_length=2, choices=REGION_CHOICES)
    author = models.CharField(max_length=50)
    date = models.DateField()
    details = models.CharField(max_length=128)

    def __str__(self):
        return self.headline
