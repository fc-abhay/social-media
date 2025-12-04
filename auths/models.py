from django.db import models
import uuid

# Create your models here.
class Auth(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fullName = models.CharField(max_length=255)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username