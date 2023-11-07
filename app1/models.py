from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=100)
    price=models.IntegerField()

    def is_expensive(self):
        if self.price>100:
            return True
        else:
            return False
