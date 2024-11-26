import django_eventstream
from django.urls import path
from django.urls.conf import include

from .views import SnortLogView


urlpatterns = [
    path('', SnortLogView.as_view()),
    path('events/', include(django_eventstream.urls), {'channels': ['snort']}),
]