from rest_framework import serializers

from notifications.models import (
    UserNotification,
    UserNotificationOption,
    NotificationTemplate,
)
from notifications.services.notification_service import NotificationService
from notifications.constants import NotificationType, Status


class UserNotificationOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserNotificationOption
        fields = ['field_id', 'txt']


class UserNotificationSerializer(serializers.ModelSerializer):
    text = serializers.SerializerMethodField()
    options = UserNotificationOptionSerializer(many=True, read_only=True)

    class Meta:
        model = UserNotification
        fields = ['id', 'text', 'status', 'notification_type', 'created', 'options']

    def get_text(self, obj):
        service = NotificationService()
        return service.render_notification_text(obj)


class CreateNotificationSerializer(serializers.Serializer):
    template_id = serializers.IntegerField()
    notification_type = serializers.ChoiceField(
        choices=NotificationType.choices
    )
    parameters = serializers.ListField(
        child=serializers.CharField(), allow_empty=True
    )

    def validate_template_id(self, value):
        if not NotificationTemplate.objects.filter(id=value).exists():
            raise serializers.ValidationError("NotificationTemplate with this ID does not exist.")
        return value

    def create(self, validated_data):
        user = self.context['request'].user
        service = NotificationService()
        notification = service.create_notification(
            user=user,
            template_id=validated_data['template_id'],
            notification_type=validated_data['notification_type'],
            parameters=validated_data['parameters']
        )
        if notification:
            return notification
        else:
            raise serializers.ValidationError("Notification was not created due to user settings.")
