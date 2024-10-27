from django.db import models


class NotificationType(models.IntegerChoices):
    SYSTEM_NOTIFICATION = 1, 'System Notification'
    PUSH_NOTIFICATION = 2, 'Push Notification'


class Status(models.IntegerChoices):
    UNREAD = 0, 'Unread'
    READ = 1, 'Read'
