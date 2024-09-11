# item/migrations/0017_remove_nonmedicalitem_company_and_more.py
# Generated by Django 5.0.7 on 2024-07-30 22:28

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0006_alter_medicalrepresentative_mobile_number'),
        ('gst', '0003_alter_gst_percentage'),
        ('item', '0016_medicine_type_nonmedicalitem_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nonmedicalitem',
            name='company',
        ),
        migrations.RemoveField(
            model_name='nonmedicalitem',
            name='division',
        ),
        migrations.RemoveField(
            model_name='nonmedicalitem',
            name='gst',
        ),
        migrations.RemoveField(
            model_name='nonmedicalitem',
            name='hsn',
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('item_type', models.CharField(choices=[('medicine', 'Medicine'), ('nonmedicalitem', 'Non-Medical Item')], max_length=50)),
                ('sku', models.CharField(max_length=10, unique=True, validators=[django.core.validators.RegexValidator('^\\d{0,10}$', 'SKU must be between 0 to 10 digits')])),
                ('image', models.ImageField(blank=True, null=True, upload_to='item_images/')),
                ('sold_loose', models.BooleanField(default=False)),
                ('sold_online', models.BooleanField(default=False)),
                ('mrp', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('purchase_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('selling_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('landing_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('use', models.CharField(blank=True, max_length=255, null=True)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(choices=[('A', 'Active'), ('D', 'Discontinued'), ('B', 'Banned')], default='A', max_length=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('dosage_form', models.CharField(blank=True, max_length=100, null=True)),
                ('packing', models.CharField(blank=True, max_length=100, null=True)),
                ('strength', models.CharField(blank=True, max_length=100, null=True)),
                ('batch_number', models.CharField(blank=True, max_length=100, null=True)),
                ('expiry_date', models.DateField(blank=True, null=True)),
                ('prescription_required', models.BooleanField(blank=True, default=True, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='company.company')),
                ('division', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='company.division')),
                ('gst', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gst.gst')),
                ('hsn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gst.hsn')),
            ],
        ),
        migrations.DeleteModel(
            name='Medicine',
        ),
        migrations.DeleteModel(
            name='NonMedicalItem',
        ),
    ]
