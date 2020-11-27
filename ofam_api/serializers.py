from rest_framework import serializers
from .models import Event, Exhibition, Ticket


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ('name', 'description', 'date', 'price')


class ExhibitionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Exhibition
        fields = ('name', 'description', 'start_date', 'end_date', 'archive')


class TicketSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ticket
        fields = ('name', 'description', 'price')
