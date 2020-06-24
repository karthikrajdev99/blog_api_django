from django.db import models
from django.contrib.auth import get_user_model
from posts.models import Post

User = get_user_model()

class Comment(models.Model):
    """Model For The Comments In The Blog Posts"""

    commenter = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments', related_query_name='comment')
    body = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments', related_query_name='comment')
    is_displayed = models.BooleanField(default=True)
    published_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Post - "{self.post.title}", Body - "{self.body}"'