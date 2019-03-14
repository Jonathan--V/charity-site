from django.urls import path, include
from rest_framework.routers import DefaultRouter

from events import views
from events.views import EventViewSet, EventList, EventDetail

router = DefaultRouter()
router.register(r'events', views.EventViewSet)

urlpatterns = [
    path('', EventList.as_view(), name='events_url_name'),
    path('<int:pk>/', EventDetail.as_view(), name='events_detail_url_name'),
    path('api/', include(router.urls)),
]