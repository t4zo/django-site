from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class Comment(models.Model):
  user_name = models.CharField(max_length=120)
  user_email = models.EmailField()
  text = models.TextField(max_length=300)
  post = models.ForeignKey('Post', on_delete=models.DO_NOTHING, related_name='comments')

  def __str__(self):
    return f'{self.user_name}  - {self.post.title}'
  