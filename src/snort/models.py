from django.db import models


class SnortType(models.IntegerChoices):
    HTTP = 1000001, 'HTTP'
    DNS = 1000002, 'DNS'
    ICMP = 1000003, 'ICMP'
    SQL_INJECTION = 1000004, 'SQL_INJECTION'


class SnortLog(models.Model):
    sid = models.IntegerField()
    type = models.CharField(choices=SnortType.choices, max_length=20)
    ip = models.CharField(max_length=16)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ip
