from notifications.constants import NotificationType, Status
from notifications.models import (
    NotificationTemplate,
    UserNotification,
    UserNotificationOption,
    UserNotificationSetting,
)


class NotificationService:
    def create_notification(self, user, template_id, notification_type, parameters):
        try:
            template = NotificationTemplate.objects.get(id=template_id)
        except NotificationTemplate.DoesNotExist:
            return None

        if not self.should_send_notification(user, template, notification_type):
            return None

        user_notification = UserNotification.objects.create(
            user=user,
            notification_template=template,
            notification_type=notification_type,
            status=Status.UNREAD,
        )

        for idx, param in enumerate(parameters, start=1):
            UserNotificationOption.objects.create(
                user_notification=user_notification,
                field_id=idx,
                txt=param
            )

        return user_notification

    def should_send_notification(self, user, template, notification_type):
        try:
            setting = UserNotificationSetting.objects.get(
                user=user,
                notification_template=template
            )
            if notification_type == NotificationType.SYSTEM_NOTIFICATION:
                return setting.system_notification
            elif notification_type == NotificationType.PUSH_NOTIFICATION:
                return setting.push_notification
            else:
                return True
        except UserNotificationSetting.DoesNotExist:
            return True

    def render_notification_text(self, notification):
        user_language = notification.user.language

        translations = notification.notification_template.translations.filter(language=user_language)
        if translations.exists():
            template_text = translations.first().text
        else:
            template_text = notification.notification_template.txt
        options = {str(option.field_id): option.txt for option in notification.options.all()}

        try:
            formatted_text = template_text
            for key, value in options.items():
                formatted_text = formatted_text.replace(f"{{{key}}}", value)
        except KeyError:
            formatted_text = template_text

        return formatted_text

    def mark_notifications_as_read(self, notifications):
        notifications.update(status=Status.READ)
