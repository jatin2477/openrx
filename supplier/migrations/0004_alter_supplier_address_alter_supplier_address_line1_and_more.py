# supplier/migrations/0004_alter_supplier_address_alter_supplier_address_line1_and_more.py
# Generated by Django 5.0.7 on 2024-07-18 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0003_supplier_address_line1_supplier_address_line2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='address_line1',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='country',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
