# Generated by Django 3.1.1 on 2020-09-30 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0010_auto_20200930_1451'),
    ]

    operations = [
        migrations.AddField(
            model_name='success',
            name='SVideo',
            field=models.FileField(blank=True, null=True, upload_to='success/videos/', verbose_name='Video upload'),
        ),
    ]