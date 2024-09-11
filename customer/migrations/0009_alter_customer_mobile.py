# customer/migrations/0009_alter_customer_mobile.py
# Generated by Django 5.0.7 on 2024-07-18 01:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0008_alter_customer_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='mobile',
            field=models.CharField(default='9823893740', max_length=10, validators=[django.core.validators.RegexValidator('^\\d{1,10}$', 'Only numeric characters are allowed.')]),
        ),
    ]
