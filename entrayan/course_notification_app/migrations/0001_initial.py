# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AlertInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('alert_type', models.CharField(max_length=50)),
                ('alert_status', models.CharField(max_length=50)),
                ('alert_for', models.CharField(max_length=100)),
                ('sent_date', models.DateTimeField(auto_now=True)),
                ('sent_to', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CourseInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('course_name', models.CharField(max_length=200)),
                ('course_duration', models.TimeField(auto_now_add=True)),
                ('course_date', models.DateTimeField()),
                ('author_name', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SubscriberInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('course_subscribed', models.CharField(max_length=200)),
                ('course_date', models.DateTimeField()),
                ('subscribed_date', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(to='course_notification_app.CourseInfo')),
                ('subscriber', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
