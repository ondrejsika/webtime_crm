# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-22 08:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('in_queue', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=32)),
                ('subject_template', models.CharField(max_length=128)),
                ('body_template', models.TextField()),
                ('is_html', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='CampaignEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('in_queue', models.BooleanField(default=False)),
                ('email_to', models.EmailField(max_length=254)),
                ('variables', models.TextField(default='{}')),
                ('rendered_subject', models.CharField(blank=True, max_length=128, null=True)),
                ('rendered_body', models.TextField(blank=True, null=True)),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailing.Campaign')),
            ],
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=32)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ListEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('email', models.EmailField(max_length=254)),
                ('is_unsubscribed', models.BooleanField(default=False)),
                ('list', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mailing.List')),
            ],
        ),
        migrations.CreateModel(
            name='QueueEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_to', models.EmailField(max_length=254)),
                ('email_from', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=128)),
                ('body', models.TextField()),
                ('is_html', models.BooleanField(default=False)),
                ('is_sent', models.BooleanField(default=False)),
                ('is_failed', models.BooleanField(default=False)),
                ('campaign', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mailing.Campaign')),
            ],
        ),
        migrations.CreateModel(
            name='Unsubscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailing.Campaign')),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailing.ListEmail')),
            ],
        ),
        migrations.AddField(
            model_name='campaign',
            name='list',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mailing.List'),
        ),
        migrations.AddField(
            model_name='campaign',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
