# Generated by Django 4.2.4 on 2023-08-23 02:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0002_album_document_alter_topic_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Album',
        ),
        migrations.DeleteModel(
            name='Document',
        ),
    ]