# Generated by Django 3.0.2 on 2020-02-22 16:29

import datetime
from django.conf import settings
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('livebit', '0018_auto_20200222_2156'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PostLikes',
            new_name='PostLike',
        ),
        migrations.AlterField(
            model_name='post',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 22, 16, 29, 20, 572676, tzinfo=utc)),
        ),
    ]
