from django.db import models

# this is how django know that 'drinks' is a model class
class Drink(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name + ': ' + self.description