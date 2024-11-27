from django.db.transaction import atomic
from django_eventstream import send_event
from rest_framework import serializers

from .models import SnortLog, SnortType


class SnortLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = SnortLog
        fields = '__all__'
        extra_kwargs = {
            'type': {'required': False},
        }

    @atomic
    def create(self, data):
        type = SnortType(data.get('sid')).label
        log = SnortLog.objects.create(**data, type=type)
        send_event(
            channel="snort",
            event_type="snort log",
            data={
                'type': type,
                'ip': log.ip,
                'date': log.date,
            }
        )
        return log