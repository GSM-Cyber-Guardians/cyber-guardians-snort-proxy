from django.db import models


class SnortSid(models.TextChoices):
    pass


class SnortLog(models.Model):
    sid = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
