from rest_framework import serializers

from .models import SnortLog


class SnortLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = SnortLog
        fields = '__all__'
