from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class Certificate(models.Model):
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=100)
    image = models.FileField(upload_to='img')
    timestamp = models.DateTimeField(auto_now_add=True)
    evidence_of_death = models.FileField(upload_to='docs',null=True)

    def __str__(self):
        return self.title

