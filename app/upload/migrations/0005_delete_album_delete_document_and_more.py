# Generated by Django 4.2.4 on 2023-08-26 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0004_documentlist_photolist'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Album',
        ),
        migrations.DeleteModel(
            name='Document',
        ),
        migrations.RemoveField(
            model_name='documentlist',
            name='document',
        ),
        migrations.AddField(
            model_name='documentlist',
            name='file',
            field=models.FileField(blank=True, upload_to='upload/document/file/', verbose_name='ファイル'),
        ),
        migrations.AlterField(
            model_name='photolist',
            name='photo',
            field=models.ImageField(blank=True, upload_to='upload/album/photo/', verbose_name='フォト'),
        ),
    ]