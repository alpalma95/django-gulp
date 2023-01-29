from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="blog-index"),
    path('posts/', views.get_all_posts, name="get-all-posts"),
    path('posts/<slug:slug>', views.get_posts_by_slug, name="get-post-by-slug")
]
