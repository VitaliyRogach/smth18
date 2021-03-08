from django.contrib.postgres.fields import JSONField
from django.db import models


class InputModel(models.Model):
    field = models.CharField(max_length=30)
    data = JSONField()

    def __str__(self):
        return self.data, self.field