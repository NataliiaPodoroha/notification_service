from django.contrib import admin
from .models import (
    User,
    UserRole,
    Language,
    NotificationCategory,
    NotificationTemplate,
    UserNotification,
    UserNotificationOption,
    UserNotificationSetting,
    TranslationString,
    Project,
    Country,
)

admin.site.register(User)
admin.site.register(UserRole)
admin.site.register(Language)
admin.site.register(NotificationCategory)
admin.site.register(NotificationTemplate)
admin.site.register(UserNotification)
admin.site.register(UserNotificationOption)
admin.site.register(UserNotificationSetting)
admin.site.register(TranslationString)
admin.site.register(Project)
admin.site.register(Country)
