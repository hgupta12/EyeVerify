from django.db import models

# Create your models here.

def upload_to(instance,filename):
    return 'images/{filename}'.format(filename=filename)

class Content(models.Model):
    text = models.TextField()
    image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)
    private = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
    