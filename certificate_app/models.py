from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class CustomUser()

class Certificate(models.Model):
    # user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.FileField(upload_to='img')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
