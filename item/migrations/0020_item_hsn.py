# item/migrations/0020_item_hsn.py
# Generated by Django 5.0.7 on 2024-07-31 22:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0019_remove_item_hsn'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='hsn',
            field=models.CharField(blank=True, max_length=8, null=True, validators=[django.core.validators.RegexValidator('^\\d{2,8}$', 'HSN must be 2 to 8 digits')]),
        ),
    ]
