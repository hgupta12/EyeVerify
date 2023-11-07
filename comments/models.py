from django.db import models
from content.models import Content
from users.models import UserData

# Create your models here.

class Comment(models.Model):
    message = models.CharField(max_length=250)
    owner = models.ForeignKey(UserData, on_delete=models.CASCADE)
    content_id = models.ForeignKey(Content, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
