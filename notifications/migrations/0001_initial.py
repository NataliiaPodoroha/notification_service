# Generated by Django 5.1.2 on 2024-10-27 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, null=True)),
                ('code', models.CharField(max_length=5, null=True)),
                ('code_exp', models.CharField(max_length=5, null=True)),
            ],
            options={
                'db_table': 'country',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, null=True)),
                ('title', models.CharField(max_length=32, null=True)),
            ],
            options={
                'db_table': 'language',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NotificationCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, null=True)),
                ('title', models.CharField(max_length=32, null=True)),
            ],
            options={
                'db_table': 'notification_category',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NotificationTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('txt', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'notification_template',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=510, null=True)),
                ('address', models.CharField(max_length=510, null=True)),
                ('started', models.DateTimeField()),
                ('lat', models.FloatField(null=True)),
                ('lng', models.FloatField(null=True)),
                ('archived', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'project',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TranslationString',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.IntegerField()),
                ('translation_field_id', models.IntegerField(choices=[(1, 'name'), (2, 'title'), (3, 'description'), (4, 'text'), (5, 'question'), (6, 'answer'), (7, 'additional')], default=1)),
                ('text', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'translation_string',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, null=True)),
                ('last_name', models.CharField(max_length=255, null=True)),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('role_id', models.PositiveIntegerField(null=True)),
                ('password', models.CharField(max_length=128, null=True)),
                ('active', models.BooleanField(default=False)),
                ('verified', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_type', models.IntegerField(choices=[(1, 'System Notification'), (2, 'Push Notification')], default=1)),
                ('status', models.IntegerField(choices=[(0, 'Unread'), (1, 'Read')], default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'user_notification',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserNotificationOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_id', models.IntegerField(null=True)),
                ('txt', models.CharField(max_length=255, null=True)),
            ],
            options={
                'db_table': 'user_notification_option',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserNotificationSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('system_notification', models.BooleanField(default=True)),
                ('push_notification', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'user_notification_setting',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'user_role',
                'managed': False,
            },
        ),
    ]
