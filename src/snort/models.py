from django.db import models


class SnortType(models.IntegerChoices):
    HTTP = 1, 'HTTP'
    ICMP = 2, 'ICMP'
    DNS = 3, 'DNS'
    SQL_INJECTION = 4, 'SQL_INJECTION'


class SnortLog(models.Model):
    sid = models.IntegerField()
    type = models.CharField(choices=SnortType.choices, max_length=20)
    ip = models.CharField(max_length=16)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ip
