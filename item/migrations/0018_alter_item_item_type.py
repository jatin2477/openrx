# item/migrations/0018_alter_item_item_type.py
# Generated by Django 5.0.7 on 2024-07-30 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0017_remove_nonmedicalitem_company_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_type',
            field=models.CharField(choices=[('medicine', 'Medicine'), ('nonmedicalitem', 'Non-Medical Item')], default='medicine', max_length=50),
        ),
    ]
