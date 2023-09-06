from django.db import models

# Create your models here.

class Content(models.Model):
    text = models.TextField()
    private = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
    