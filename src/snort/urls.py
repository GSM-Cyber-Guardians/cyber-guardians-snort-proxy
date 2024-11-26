from django.urls import path

from .views import SnortLogView


urlpatterns = [
    path('', SnortLogView.as_view())
]