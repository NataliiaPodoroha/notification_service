from django.urls import path, include
from rest_framework.routers import DefaultRouter
from notifications.views import UserNotificationViewSet
from rest_framework.authtoken import views

router = DefaultRouter()
router.register('', UserNotificationViewSet, basename='notifications')

urlpatterns = [
    path('', include(router.urls)),
    # path('login/', views.obtain_auth_token, name='login'),
]

app_name = "notifications"
