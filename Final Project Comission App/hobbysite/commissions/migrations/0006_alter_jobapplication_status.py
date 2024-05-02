# Generated by Django 5.0.4 on 2024-05-01 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commissions', '0005_alter_job_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplication',
            name='status',
            field=models.CharField(choices=[('AP', 'Pending'), ('BP', 'Accepted'), ('CR', 'Rejected')], default='AP', max_length=9),
        ),
    ]