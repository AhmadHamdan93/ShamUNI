# Generated by Django 3.1.1 on 2020-09-30 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0007_auto_20200827_0122'),
    ]

    operations = [
        migrations.AddField(
            model_name='adds',
            name='APDF',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
