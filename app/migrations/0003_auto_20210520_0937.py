# Generated by Django 2.2 on 2021-05-20 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_files'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='resume',
            field=models.FileField(upload_to='assets/mediafiles'),
        ),
    ]
