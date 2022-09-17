from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class QueryHolder(models.Model):
    # query_by = models.ForeignKey(User, on_delete=models.CASCADE)
    query = models.TextField(blank=True)

    def __str__(self):
        return self.query