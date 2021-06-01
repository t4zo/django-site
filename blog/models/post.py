from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
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

  