from rest_framework import serializers

from events.models.events.event import Event


class EventSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = Event
        fields = '__all__'
