# Generated by Django 3.2 on 2022-11-16 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20221116_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(default='-', max_length=10),
        ),
    ]
