from django.shortcuts import render

# Create your views here.
from django.views import generic
from rest_framework import viewsets, permissions
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from events.models.events.event import Event
from events.permissions import IsOwnerOrReadOnly
from events.serializers.events.event_serializer import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class EventList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'events/event_list.html'

    def get_queryset(self):
        return Event.objects.all()

    def get(self, request):
        return Response({'events': self.get_queryset()})


class EventDetail(generic.DetailView):
    model = Event
