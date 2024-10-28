from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from notifications.models import UserNotification
from notifications.serializers import (
    UserNotificationSerializer,
    CreateNotificationSerializer
)
from notifications.services.notification_service import NotificationService


class UserNotificationViewSet(viewsets.ModelViewSet):
    queryset = UserNotification.objects.all()

    def get_queryset(self):
        user_id = self.request.query_params.get("user_id")

        queryset = UserNotification.objects.filter(user_id=user_id)

        notification_type = self.request.query_params.get('notification_type')
        status_param = self.request.query_params.get('status')

        if notification_type:
            queryset = queryset.filter(notification_type=notification_type)
        if status_param:
            queryset = queryset.filter(status=status_param)

        return queryset.order_by('-created')

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateNotificationSerializer
        else:
            return UserNotificationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        notification = serializer.save()
        return Response(
            {"detail": "Notification created successfully."},
            status=status.HTTP_201_CREATED
        )

    @action(detail=False, methods=['post'], url_path='mark-as-read')
    def mark_as_read(self, request):
        notification_ids = request.data.get('ids', [])
        notifications = UserNotification.objects.filter(
            user=request.user,
            id__in=notification_ids
        )
        service = NotificationService()
        service.mark_notifications_as_read(notifications)
        return Response(
            {"detail": "Notifications marked as read."},
            status=status.HTTP_200_OK
        )
