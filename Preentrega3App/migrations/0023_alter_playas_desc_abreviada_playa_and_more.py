# Generated by Django 4.1.7 on 2023-06-30 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Preentrega3App', '0022_rename_desc_abreviada_playas_desc_abreviada_playa_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playas',
            name='desc_abreviada_playa',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='playas',
            name='descripcion_playa',
            field=models.CharField(max_length=1200),
        ),
    ]