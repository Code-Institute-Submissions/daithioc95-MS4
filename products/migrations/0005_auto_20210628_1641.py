# Generated by Django 3.2.4 on 2021-06-28 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20210628_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='AccessionYear',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='Period',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]