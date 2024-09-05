# Generated by Django 5.0.7 on 2024-07-26 22:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0006_alter_medicalrepresentative_mobile_number'),
        ('gst', '0002_remove_gst_gst_type_alter_gst_percentage'),
        ('item', '0002_alter_medicine_image_alter_medicine_landing_cost_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='gst',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gst.gst'),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='hsn',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gst.hsn'),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='marketed_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company'),
        ),
        migrations.AlterField(
            model_name='nonmedicalitem',
            name='gst',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gst.gst'),
        ),
        migrations.AlterField(
            model_name='nonmedicalitem',
            name='hsn',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gst.hsn'),
        ),
        migrations.AlterField(
            model_name='nonmedicalitem',
            name='marketed_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company'),
        ),
    ]
