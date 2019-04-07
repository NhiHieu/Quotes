from django.db import models
from django.contrib.auth.models import User
from model_utils.models import TimeStampedModel
# Create your models here.


class Quote(TimeStampedModel):
    author = models.CharField(max_length=128, default='')
    content = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.author


