# Generated by Django 4.2.3 on 2023-08-05 00:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_address_zip'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='desciption',
            new_name='description',
        ),
    ]
