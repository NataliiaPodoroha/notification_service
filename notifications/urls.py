from django.urls import path, include
from rest_framework.routers import DefaultRouter
from notifications.views import UserNotificationViewSet

router = DefaultRouter()
router.register('', UserNotificationViewSet, basename='notifications')

urlpatterns = [
    path('', include(router.urls)),
]

app_name = "notifications"
