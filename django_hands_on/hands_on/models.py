from django.db import models

class Drink(models.Model):  # That is how the django knows it is a model class 
    """
    Each drink will have a name and a description
    """
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500) 

    def __str__(self):
        return self.name + ':  ' + self.description
 