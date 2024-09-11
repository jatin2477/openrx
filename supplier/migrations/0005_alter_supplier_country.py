# supplier/migrations/0005_alter_supplier_country.py
# Generated by Django 5.0.7 on 2024-07-18 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0004_alter_supplier_address_alter_supplier_address_line1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='country',
            field=models.CharField(default='India', max_length=100),
        ),
    ]
