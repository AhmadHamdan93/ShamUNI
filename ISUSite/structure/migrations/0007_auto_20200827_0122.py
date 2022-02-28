# Generated by Django 3.0.7 on 2020-08-26 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0006_doctors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctors',
            name='DCareer',
            field=models.CharField(max_length=100, verbose_name='career'),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='DFacebook',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Facebook'),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='DLinkedin',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Linked in'),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='DName',
            field=models.CharField(max_length=100, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='DTwitter',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Twitter'),
        ),
    ]