# Generated by Django 3.1.3 on 2020-11-29 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='all_items',
            new_name='order_list',
        ),
    ]
