# Generated by Django 5.0 on 2023-12-30 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_posts_dislike_posts_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='slug',
            field=models.SlugField(default=1, max_length=300),
            preserve_default=False,
        ),
    ]
