# Generated by Django 4.1.7 on 2023-06-29 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Preentrega3App', '0019_alter_avatar_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Presentacion',
            new_name='Cabecera',
        ),
        migrations.RenameField(
            model_name='cabecera',
            old_name='img_senderismo',
            new_name='img_cabecera',
        ),
        migrations.RenameField(
            model_name='cabecera',
            old_name='texto',
            new_name='texto_cabecera',
        ),
        migrations.RenameField(
            model_name='cabecera',
            old_name='titulo',
            new_name='titulo_cabecera',
        ),
        migrations.AlterField(
            model_name='avatar',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Preentrega3App.userprofile'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
