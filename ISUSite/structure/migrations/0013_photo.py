# Generated by Django 3.1.1 on 2020-10-03 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0012_auto_20201003_2215'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PName', models.CharField(max_length=100, verbose_name='Image Name')),
                ('PImage', models.ImageField(upload_to='gallery/', verbose_name='Upload Image')),
            ],
        ),
    ]