# Generated by Django 4.1.7 on 2023-07-01 20:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Preentrega3App', '0027_alter_userprofile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Avatar',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
