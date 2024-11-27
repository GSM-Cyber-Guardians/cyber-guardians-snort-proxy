from django.db.transaction import atomic
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import SnortLog
from .serializers import SnortLogSerializer


class SnortLogView(APIView):
    def get(self, request: Request) -> Response:
        log = SnortLog.objects.all()
        serializer = SnortLogSerializer(log, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @atomic
    def post(self, request: Request) -> Response:
        serializer = SnortLogSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
