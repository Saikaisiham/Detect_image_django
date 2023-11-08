from django.db import models

# Create your models here.
class Message(models.Model):
    message = models.TextField()
    consumed_at = models.DateTimeField(auto_now_add=True)