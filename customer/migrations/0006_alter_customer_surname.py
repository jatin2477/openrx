# Generated by Django 5.0.7 on 2024-07-17 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_alter_customer_surname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='surname',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
