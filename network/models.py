from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    followers = models.IntegerField(default=0)

class Post(models.Model):
    author = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)

    def serialize(self):
        return {
        "id": {self.id},
        "author_id": {self.author.id},
        "content": {self.content},
        "timestamp": {self.timestamp},
        "likes": {self.likes}
        }

    def __str__(self):
        return f"""
        id: {self.id}
        author_id: {self.author.id}
        content: {self.content}
        timestamp: {self.timestamp}
        likes: {self.likes}
        """

class Comment(models.Model):
    author = models.ForeignKey("User", related_name="comments", on_delete=models.CASCADE)
    post = models.ForeignKey("Post", related_name="comments", on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)


    def serialize(self):
        return {
        "id": {self.id},
        "author_id": {self.author.id},
        "post_id": {self.post.id},
        "content": {self.content},
        "timestamp": {self.timestamp}
        }

    def __str__(self):
        return f"""
        id: {self.id}
        author_id: {self.author.id}
        content: {self.content}
        post_id: {self.post.id}
        timestamp: {self.timestamp}
        """

class Post_Feedback(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="post_feedback")
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="post_feedback", blank=True)
    liked = models.BooleanField(default=False)
    unliked = models.BooleanField(default=False)

    def serialize(self):
        return {
        "id": {self.id},
        "user": {self.user.id},
        "post_id": {self.post.id},
        "liked": {self.liked},
        "unliked": {self.unliked}
        }

    def __str__(self):
        return f"""
        id: {self.id}
        user_id: {self.user.id}
        liked: {self.liked}
        unliked: {self.unliked}
        post_id: {self.post.id}
        """

class Following_List(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="following_list")
    following = models.ManyToManyField(User, blank=True, related_name="followers_list")

    def serialize(self):
        return {
        "id": {self.id},
        "user": {self.user.id},
        "following_users_id's": {[user.id for user in self.following.all()]}
        }

    def __str__(self):
        return f"""
        id: {self.id}
        user_id: {self.user.id}
        following_users_id's: {[user.id for user in self.following.all()]}
        """