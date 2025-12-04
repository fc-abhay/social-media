from django.db import models
from auths.models import Auth  # Import your user model
import uuid

class Post(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content = models.TextField()
    createdBy = models.ForeignKey(Auth, on_delete=models.CASCADE, related_name='posts', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content[:30]  # first 30 chars


class Comment(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    createdBy = models.ForeignKey(Auth, on_delete=models.CASCADE, related_name='comments',null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.createdBy.username} on {self.post}'


class Like(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
    createdBy = models.ForeignKey(Auth, on_delete=models.CASCADE, related_name='likes',null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Like by {self.createdBy.username} on {self.post}'
