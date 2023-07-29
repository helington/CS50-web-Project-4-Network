from django.contrib import admin

from .models import User, Post, Comment, Following_List, Post_Feedback
# Register your models here.

admin.site.register(User)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Following_List)
admin.site.register(Post_Feedback)