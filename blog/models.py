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

class Post(models.Model):
  title = models.CharField(max_length=100)
  date = models.DateField()
  image = models.ImageField(upload_to='posts', null=True)
  excerpt = models.CharField(max_length=255)
  content = models.TextField(validators=[MinLengthValidator(10)])
  author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True, related_name='posts')
  slug = models.SlugField()
  tags = models.ManyToManyField('Tag', related_name='posts')

  def __str__(self):
    return f"{self.title}"


class Tag(models.Model):
  caption = models.CharField(max_length=20)

  def __str__(self):
    return self.caption


class Comment(models.Model):
  user_name = models.CharField(max_length=120)
  user_email = models.EmailField()
  text = models.TextField(max_length=300)
  post = models.ForeignKey('Post', on_delete=models.DO_NOTHING, related_name='comments')

  def __str__(self):
    return f'{self.user_name}  - {self.post.title}'
  