from django.db import models

category_choice = [
    ("SN", "SCIENCE"),
    ("HC", "HISTORICAL"),
    ("ST", "STORY"),
]

class Book(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    author = models.CharField(max_length=30)
    category = models.CharField(max_length=2,choices=category_choice)  
    def __str__(self):
        return self.name