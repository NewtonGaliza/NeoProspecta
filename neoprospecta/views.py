from neoprospecta.models import Entry
from neoprospecta.serializers import EntrySerializer

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets

class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer

    
