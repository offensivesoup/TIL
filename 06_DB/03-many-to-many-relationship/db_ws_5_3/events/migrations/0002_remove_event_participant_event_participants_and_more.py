# Generated by Django 4.2.11 on 2024-04-08 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='participant',
        ),
        migrations.AddField(
            model_name='event',
            name='participants',
            field=models.ManyToManyField(related_name='events', to='events.participant'),
        ),
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='participant',
            name='registration_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
