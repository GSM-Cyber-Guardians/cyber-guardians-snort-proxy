from django.db.transaction import atomic
from django_eventstream import send_event
from rest_framework import serializers

from .models import SnortLog, snort_type


class SnortLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = SnortLog
        fields = '__all__'
        extra_kwargs = {
            'type': {'required': False},
        }

    @atomic
    def create(self, data):
        sid = data.get('sid')
        detected_type = snort_type.get(sid)
        return SnortLog.objects.create(**data, type=detected_type)

    def send_event(self, data, obj):
        type = snort_type.get(data['sid'])
        send_event(
            channel="snort",
            event_type="event",
            data={
                'type': type,
                'ip': obj.ip,
                'date': obj.date,
            }
        )