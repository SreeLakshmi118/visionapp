# Generated by Django 4.1.6 on 2023-03-01 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visionapp', '0002_alter_reads_audio_alter_reads_author_alter_reads_img_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='language',
            options={'default_permissions': ()},
        ),
    ]