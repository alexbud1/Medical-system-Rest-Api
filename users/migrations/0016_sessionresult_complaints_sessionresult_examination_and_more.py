# Generated by Django 4.0.6 on 2022-07-29 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_alter_doctor_organization'),
    ]

    operations = [
        migrations.AddField(
            model_name='sessionresult',
            name='complaints',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='sessionresult',
            name='examination',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='sessionresult',
            name='payer',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='sessionresult',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sessionresult',
            name='treatment',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='sessionresult',
            name='diagnosis',
            field=models.CharField(blank=True, default=None, max_length=400, null=True),
        ),
    ]
