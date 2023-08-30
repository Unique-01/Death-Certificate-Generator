from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class DeathRecord(models.Model):
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,null=True)
    deceased_name = models.CharField(max_length=100)
    death_date = models.DateField()
    death_location = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    image = models.FileField(upload_to='img')
    timestamp = models.DateTimeField(auto_now_add=True)
    evidence_of_death = models.FileField(upload_to='docs',null=True)

    def __str__(self):
        return self.deceased_name
