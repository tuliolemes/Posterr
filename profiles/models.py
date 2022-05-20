from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
# # Create your models here.

class Profile(models.Model):
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #username = models.CharField(max_length=14, validators=[alphanumeric])
    following = models.ManyToManyField(User, related_name='following', blank=True)
    #NumberOfFollowers = models.BigIntegerField()
    joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    def profiles_posts(self):
        return self.post_set.all()

    class Meta:
        ordering = ['-joined']


