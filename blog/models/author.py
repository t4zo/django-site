from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class Author(models.Model):
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  email = models.EmailField()

  def full_name(self):
    return f"{self.first_name} {self.last_name}"

  def __str__(self):
      return self.full_name()
  