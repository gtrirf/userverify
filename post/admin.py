from django.contrib import admin
from .models import Post, PostLike, PostComment, CommentLike


admin.site.register(Post)
admin.site.register(PostComment)
admin.site.register(PostLike)
admin.site.register(CommentLike)