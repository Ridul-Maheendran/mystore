from django.db import models
from django.contrib.auth.models import User

from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.
class Products(models.Model):

    name = models.CharField(max_length=30)
    prize = models.PositiveIntegerField()
    discription = models.CharField(max_length=200)
    category = models.CharField(max_length=50)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.name
    
class Carts(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product =models.ForeignKey(Products,on_delete=models.CASCADE)
    date = models.DateTimeField( auto_now_add=True)


class Reviews(models.Model):
  product =models.ForeignKey(Products,on_delete=models.CASCADE)  
  user = models.ForeignKey(User,on_delete=models.CASCADE)
  rating = models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
  commands= models.CharField(max_length=200)

  def __str__(self):
      return self.commands
