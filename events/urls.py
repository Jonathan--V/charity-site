from django.urls import path, include
from rest_framework.routers import DefaultRouter

from events.views import EventViewSet, EventList, EventDetail

router = DefaultRouter()
router.register('events', EventViewSet)

urlpatterns = [
    path('', EventList.as_view(), name='events_url_name'),
    path('<int:pk>/', EventDetail.as_view(), name='events_detail_url_name'),
    path('api/', include(router.urls)),
]