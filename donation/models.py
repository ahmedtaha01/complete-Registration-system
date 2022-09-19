from django.db import models
from project.models import Project
from django.contrib.auth import get_user_model

# Create your models here.

class Donation(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE,related_name='donations')
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.amount
