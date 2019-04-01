from rest_framework import viewsets
from . import models
from . import serializers


class EntryViewSet(viewsets.ModelViewSet):

    queryset = models.Entry.objects.all()
    serializer_class = serializers.EntrySerializer
