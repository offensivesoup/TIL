# Generated by Django 4.2.11 on 2024-04-08 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_alter_attendance_total_fee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='total_fee',
            field=models.IntegerField(),
        ),
    ]