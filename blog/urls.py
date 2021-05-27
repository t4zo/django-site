from django.urls import path

from . import views

urlpatterns = [
  path('', views.BlogView.as_view(), name='blog'),
  path('posts', views.PostsView.as_view(), name='posts'),
  path('posts/read-later', views.ReadLaterView.as_view(), name='read-later'),
  path('posts/<slug:slug>', views.PostView.as_view(), name='post'),
]