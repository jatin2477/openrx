# Generated by Django 5.0.7 on 2024-07-13 22:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
        ('supplier', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='division',
            name='medical_representative',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='division', to='company.medicalrepresentative'),
        ),
        migrations.AlterField(
            model_name='division',
            name='suppliers',
            field=models.ManyToManyField(blank=True, related_name='divisions', to='supplier.supplier'),
        ),
    ]
