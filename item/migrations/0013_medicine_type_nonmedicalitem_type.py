# Generated by Django 5.0.7 on 2024-07-28 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0012_medicine_created_at_medicine_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicine',
            name='type',
            field=models.CharField(default='medicine', max_length=50),
        ),
        migrations.AddField(
            model_name='nonmedicalitem',
            name='type',
            field=models.CharField(default='medicine', max_length=50),
        ),
    ]
