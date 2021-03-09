# Generated by Django 3.0.2 on 2020-02-22 16:15

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('livebit', '0011_auto_20200222_2137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postlikes',
            name='postid',
        ),
        migrations.RemoveField(
            model_name='posttag',
            name='tagid',
        ),
        migrations.AddField(
            model_name='postlikes',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='post', to='livebit.Post'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 22, 16, 15, 42, 689854, tzinfo=utc)),
        ),
    ]
