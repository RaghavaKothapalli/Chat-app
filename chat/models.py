from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.CharField(max_length=100)  # 🆕 Add room
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.room}] {self.user.username}: {self.content[:20]}"
