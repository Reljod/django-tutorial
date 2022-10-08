# Generated by Django 4.1.2 on 2022-10-08 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nft',
            name='image_link',
        ),
        migrations.AddField(
            model_name='nft',
            name='image_url',
            field=models.URLField(null=True, verbose_name='image_url'),
        ),
    ]