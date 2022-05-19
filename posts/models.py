from django.db import models
from profiles.models import Profile

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    description = models.TextField(max_length=777)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description

    
    class Meta:
        ordering = ['-created']