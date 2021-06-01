from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class Tag(models.Model):
  caption = models.CharField(max_length=20)

  def __str__(self):
    return self.caption
  