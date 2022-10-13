from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class QueryHolder(models.Model):
    # query_by = models.ForeignKey(User, on_delete=models.CASCADE)
    query = models.TextField(blank=True)

    def __str__(self):
        return self.query


class HelperModel(models.Model):
    open_new = models.IntegerField(default=0)
    test_me = models.IntegerField(default=0)
    study = models.IntegerField(default=0)
    fixed = models.IntegerField(default=0)
    closed = models.IntegerField(default=0)
    multistate = models.IntegerField(default=0)

    total = models.IntegerField(default=0)


class TempDataHolder(models.Model):
    keywords = models.TextField()
    main_keywords = models.TextField()