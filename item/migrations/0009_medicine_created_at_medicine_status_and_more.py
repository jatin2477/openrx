# item/migrations/0009_medicine_created_at_medicine_status_and_more.py
# Generated by Django 5.0.7 on 2024-07-28 19:49

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0008_remove_medicine_created_at_and_more'),
    ]

    operations = [
        # migrations.AddField(
        #     model_name='medicine',
        #     name='created_at',
        #     field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
        #     preserve_default=False,
        # ),
        # migrations.AddField(
        #     model_name='medicine',
        #     name='status',
        #     field=models.CharField(choices=[('A', 'Active'), ('D', 'Discontinued'), ('B', 'Banned')], default='A', max_length=1),
        # ),
        # migrations.AddField(
        #     model_name='medicine',
        #     name='updated_at',
        #     field=models.DateTimeField(auto_now=True),
        # ),
        # migrations.AddField(
        #     model_name='nonmedicalitem',
        #     name='created_at',
        #     field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
        #     preserve_default=False,
        # ),
        # migrations.AddField(
        #     model_name='nonmedicalitem',
        #     name='status',
        #     field=models.CharField(choices=[('A', 'Active'), ('D', 'Discontinued'), ('B', 'Banned')], default='A', max_length=1),
        # ),
        # migrations.AddField(
        #     model_name='nonmedicalitem',
        #     name='updated_at',
        #     field=models.DateTimeField(auto_now=True),
        # ),
    ]
