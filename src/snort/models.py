from django.db import models
from range_key_dict import RangeKeyDict


snort_type = RangeKeyDict({
    (1000001, 1000002): 'HTTP',
    (1000002, 1000003): 'DNS',
    (1000003, 1000004): 'ICMP',
    (1000004, 1000011): 'SQL_INJECTION',
    (1000011, 1000014): 'XSS'
})


class SnortLog(models.Model):
    sid = models.IntegerField()
    type = models.CharField(max_length=20)
    ip = models.CharField(max_length=16)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ip
