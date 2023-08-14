from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    subject=models.CharField(max_length=128)
    content=models.TextField()
    is_starred=models.BooleanField(default=False)
    updated_at=models.DateTimeField(auto_now=True)
    created_at=models.DateTimeField(auto_now_add=True)
    created_by=models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")

    def __str__(self):
        return f"{self.created_by} and {self.subject}"