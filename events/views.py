# Create your views here.
from django.views import generic
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework_jwt.views import ObtainJSONWebToken, RefreshJSONWebToken

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
    permission_classes = (IsAuthenticatedOrReadOnly,
                        IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class WrapperViewSet(ViewSet):

    def __init__(self, underlying_api_view, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.underlying_api_view = underlying_api_view
        self.serializer_class = self.underlying_api_view.serializer_class

    def create(self, request, *args, **kwargs):
        self.underlying_api_view.request = request
        return self.underlying_api_view.post(request, *args, **kwargs)


class ObtainTokenWrapperViewSet(WrapperViewSet):
    permission_classes = (AllowAny,)
    def __init__(self, *args, **kwargs):
        super().__init__(ObtainJSONWebToken(), *args, **kwargs)


class RefreshTokenWrapperViewSet(WrapperViewSet):

    def __init__(self, *args, **kwargs):
        super().__init__(RefreshJSONWebToken(), *args, **kwargs)


class EventList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'events/event_list.html'

    def get_queryset(self):
        return Event.objects.all()

    def get(self, request):
        return Response({'events': self.get_queryset()})


class EventDetail(generic.DetailView):
    model = Event

