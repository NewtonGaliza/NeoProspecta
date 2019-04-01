from . import models
from rest_framework import serializers

class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Entry
        fields = {'id', 'access_id', 'kingdom', 'specie', 'sequence'}

