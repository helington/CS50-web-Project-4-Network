
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),

    #API Routes
    path("posts", views.newPost, name="post"),
    path("posts<int:post_id>", views.postById, name="postById"),
    path("posts/all", views.allPosts, name="allPosts"),
    path("posts/following", views.followingPosts, name="followingPosts"),

    path("users/<int:user_id>", views.userInfo, name="userInfo")
]
