# Generated by Django 4.0.6 on 2022-08-06 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_client_sex'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='client_of_org',
            new_name='organization',
        ),
    ]
