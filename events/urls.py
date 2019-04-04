from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from events.views import EventViewSet, EventList, EventDetail, ObtainTokenWrapperViewSet, RefreshTokenWrapperViewSet

router = DefaultRouter()
router.register('token-auth', ObtainTokenWrapperViewSet, basename='token-auth')
router.register('token-refresh', RefreshTokenWrapperViewSet, basename='token-refresh')
router.register('events', EventViewSet)

urlpatterns = [
    path('', EventList.as_view(), name='events_url_name'),
    path('<int:pk>/', EventDetail.as_view(), name='events_detail_url_name'),
    path('api/api-token-auth/', obtain_jwt_token),
    path('api/api-token-refresh/', refresh_jwt_token),
    path('api/', include(router.urls)),
]