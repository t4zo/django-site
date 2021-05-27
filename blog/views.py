from datetime import date

from django.http.response import HttpResponseRedirect
from .forms import CommentForm

from django.views.generic.base import TemplateView, View
from .models import Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

from django.shortcuts import get_object_or_404, render

class BlogView(ListView):
  template_name = 'blog/index.html'
  model = Post
  context_object_name = 'posts'

  def get_queryset(self):
      overrided_queryset = super().get_queryset().order_by('-date')[:3]
      return overrided_queryset

class PostsView(ListView):
  template_name = 'blog/posts.html'
  model = Post
  context_object_name = 'posts'
  ordering = ['-date', 'title']


class PostView(View):
  def is_stored_post(self, request, post_id):
    stored_posts = request.session.get('stored_posts')
    if stored_posts is not None:
      is_saved_for_later = post_id in stored_posts
    else:
      is_saved_for_later = False
    
    return is_saved_for_later

  def get(self, request, slug):
    post = get_object_or_404(Post, slug=slug)

    return render(request, 'blog/post.html', {
      'post': post,
      'post_tags': post.tags.all(),
      'post_comments': post.comments.order_by('-id').all(),
      'is_saved_for_later': self.is_stored_post(request, post.id),
      'form': CommentForm()
    })

  def post(self, request, slug):
    post = get_object_or_404(Post, slug=slug)
    form = CommentForm(request.POST)

    if form.is_valid():
      comment = form.save(commit=False)
      comment.post = post
      comment.save()
      return HttpResponseRedirect(reverse_lazy('post', args=[slug]))

    return render(request, 'blog/post.html', {
      'post': post,
      'post_tags': post.tags.all(),
      'post_comments': post.comments.all(),
      'is_saved_for_later': self.is_stored_post(request, post.id),
      'form': form
    })


class ReadLaterView(View):
  def get(self, request):
    stored_posts = request.session.get('stored_posts')
    context = {}
    
    if stored_posts is None or len(stored_posts) == 0:
      context['posts'] = []
      context['has_posts'] = len(context['posts']) != 0
      return render(request, 'blog/stored_posts.html', context)

    posts = Post.objects.filter(id__in=stored_posts)
    context['posts'] = posts

    context['has_posts'] = len(context['posts']) != 0

    return render(request, 'blog/stored_posts.html', context)

  def post(self, request):
    stored_posts = request.session.get('stored_posts')
    if stored_posts is None:
      stored_posts = []

    post_id = int(request.POST['post_id'])
    if post_id in stored_posts:
      stored_posts.remove(post_id)
    else:
      stored_posts.append(post_id)

    request.session['stored_posts'] = stored_posts

    return HttpResponseRedirect('/')



# def blog(request):
#     posts = Post.objects.all().order_by('-date')[:3]
#     posts_tags = []

#     # for post in posts:
#     #   posts.tags = post.tags.all()

#     return render(request, "blog/index.html", {
#       "posts": posts,
#       # "post_tags": posts_tags
#     })

# def posts(request):
#     all_posts = Post.objects.all().order_by('-date')
#     return render(request, "blog/posts.html", {
#       "posts": all_posts
#     })

# def post(request, slug):
#     identified_post = get_object_or_404(Post, slug=slug)
#     return render(request, "blog/post.html", {
#       "post": identified_post,
#       "post_tags": identified_post.tags.all()
#     })
