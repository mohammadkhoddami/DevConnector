# Generated by Django 5.0 on 2023-12-30 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_userprofile_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='photo',
            new_name='picture',
        ),
    ]