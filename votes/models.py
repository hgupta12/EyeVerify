from django.db import models
from content.models import Content
from users.models import UserData

# Create your models here.

class Vote(models.Model):
    OPTIONS = [
        (1, "True"),
        (2, "Fake")
    ]
    content_id = models.ForeignKey(Content, on_delete=models.CASCADE)
    owner = models.ForeignKey(UserData, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    choice = models.IntegerField(
        choices=OPTIONS
    )