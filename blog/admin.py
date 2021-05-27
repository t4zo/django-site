from django.contrib import admin
from .models import Author, Comment, Post, Tag

# Register your models here.
class CommentAdmin(admin.ModelAdmin):
  list_filter = ('post',)
  list_display = ('user_name', 'user_email', 'post',)

class PostAdmin(admin.ModelAdmin):
  prepopulated_fields = {'slug': ('title',)}
  list_filter = ('author', 'tags',)
  list_display = ('title', 'author', 'date',)

admin.site.register(Author)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)
