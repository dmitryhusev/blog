from django.urls import path
from .views import PostView, BlogDetailView, BlogCreateView

urlpatterns = [
    path('', PostView.as_view(), name='home'),
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post_detail"),
    path("post/new/", BlogCreateView.as_view(), name="post_new"),
]