# Generated by Django 3.2.9 on 2021-11-22 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='height',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='animal',
            name='speed',
            field=models.CharField(max_length=200),
        ),
    ]