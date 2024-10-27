from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from .constants import NotificationType, Status


class Country(models.Model):
    name = models.CharField(max_length=25, null=True)
    code = models.CharField(max_length=5, null=True)
    code_exp = models.CharField(max_length=5, null=True)

    class Meta:
        managed = False
        db_table = 'country'

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=32, null=True)
    title = models.CharField(max_length=32, null=True)

    class Meta:
        managed = False
        db_table = 'language'

    def __str__(self):
        return self.title


class NotificationCategory(models.Model):
    name = models.CharField(max_length=32, null=True)
    title = models.CharField(max_length=32, null=True)

    class Meta:
        managed = False
        db_table = 'notification_category'

    def __str__(self):
        return self.title


class NotificationTemplate(models.Model):
    notification_category = models.ForeignKey(
        NotificationCategory,
        on_delete=models.CASCADE,
        null=True
    )
    name = models.CharField(max_length=32)
    txt = models.CharField(max_length=255)
    translations = GenericRelation(
        'TranslationString',
        related_query_name='notification_templates',
    )

    class Meta:
        managed = False
        db_table = 'notification_template'

    def __str__(self):
        return self.name


class Project(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=510, null=True)
    address = models.CharField(max_length=510, null=True)
    started = models.DateTimeField()
    lat = models.FloatField(null=True)
    lng = models.FloatField(null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)
    archived = models.BooleanField(default=False)

    class Meta:
        managed = False
        db_table = 'project'

    def __str__(self):
        return self.name


class TranslationString(models.Model):
    FIELD_CHOICES = [
        (1, 'name'),
        (2, 'title'),
        (3, 'description'),
        (4, 'text'),
        (5, 'question'),
        (6, 'answer'),
        (7, 'additional'),
    ]

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.IntegerField()
    related_item = GenericForeignKey('content_type', 'object_id')
    translation_field_id = models.IntegerField(choices=FIELD_CHOICES, default=1)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'translation_string'
        unique_together = ('content_type', 'object_id', 'translation_field_id', 'language')

    def __str__(self):
        return f'Translation for {self.related_item} in {self.language.title}'


class User(models.Model):
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    email = models.EmailField(unique=True, null=True)
    role_id = models.PositiveIntegerField(null=True)
    password = models.CharField(max_length=128, null=True)
    active = models.BooleanField(default=False)
    verified = models.BooleanField(default=False)
    language = models.ForeignKey(Language, on_delete=models.SET_DEFAULT, default=1)

    class Meta:
        managed = False
        db_table = 'user'

    def __str__(self):
        return self.email


class UserNotification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    notification_template = models.ForeignKey(
        NotificationTemplate, on_delete=models.CASCADE, null=True
    )
    notification_type = models.IntegerField(
        choices=NotificationType.choices,
        default=NotificationType.SYSTEM_NOTIFICATION,
    )
    status = models.IntegerField(
        choices=Status.choices,
        default=Status.UNREAD,
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'user_notification'

    def __str__(self):
        return f'Notification for {self.user.email} - {self.notification_template.name}'


class UserNotificationOption(models.Model):
    user_notification = models.ForeignKey(
        UserNotification, on_delete=models.CASCADE, null=True, related_name='options'
    )
    field_id = models.IntegerField(null=True)
    txt = models.CharField(max_length=255, null=True)

    class Meta:
        managed = False
        db_table = 'user_notification_option'

    def __str__(self):
        return f'Option {self.field_id} for notification {self.user_notification.id}'


class UserNotificationSetting(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    notification_template = models.ForeignKey(
        NotificationTemplate, on_delete=models.CASCADE, null=True
    )
    system_notification = models.BooleanField(default=True)
    push_notification = models.BooleanField(default=True)

    class Meta:
        managed = False
        db_table = 'user_notification_setting'

    def __str__(self):
        return f'Settings for {self.user.email} - {self.notification_template.name}'


class UserRole(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_role'
