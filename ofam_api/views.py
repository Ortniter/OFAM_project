from rest_framework import viewsets, mixins

from .serializers import EventSerializer, ExhibitionSerializer
from .models import Event, Exhibition


class EventViewSet(mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    queryset = Event.objects.all().order_by('-date')
    serializer_class = EventSerializer


class ExhibitionViewSet(viewsets.ModelViewSet):
    queryset = Exhibition.objects.all().order_by('-end_date')
    serializer_class = ExhibitionSerializer
