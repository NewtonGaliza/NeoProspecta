from rest_framework import serializers
from neoprospecta.models import Entry

class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ('id', 'access_id', 'kingdom', 'specie', 'sequence')

    def create(self, validated_data):
        return Entry.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.access_id = validated_data.get('access_id', instance.access_id)
        instance.kingdom = validated_data.get('kingdom', instance.kingdom)
        instance.specie = validated_data.get('specie', instance.specie)
        instance.sequence = validated_data.get('sequence', instance.sequence)
        instance.save()
        return instance

