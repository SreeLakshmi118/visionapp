# Generated by Django 4.1.6 on 2023-03-02 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visionapp', '0003_alter_language_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reads',
            name='audio',
            field=models.FileField(max_length=500, unique=True, upload_to='audio/'),
        ),
    ]
