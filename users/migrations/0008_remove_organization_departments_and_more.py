# Generated by Django 4.0.6 on 2022-07-28 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_remove_appointment_doctor_appointment_doctor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='departments',
        ),
        migrations.AddField(
            model_name='department',
            name='organization',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='users.organization'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.doctor'),
        ),
    ]