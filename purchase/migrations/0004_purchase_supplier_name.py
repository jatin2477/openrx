# Generated by Django 5.0.7 on 2024-08-01 01:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0003_remove_purchase_supplier_name'),
        ('supplier', '0009_rename_drug_license_validity_supplier_drug_license1_validity'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='supplier_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='supplier.supplier'),
            preserve_default=False,
        ),
    ]
