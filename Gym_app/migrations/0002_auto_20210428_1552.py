# Generated by Django 3.1.7 on 2021-04-28 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Gym_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exercises',
            old_name='names',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='exercises',
            name='names1',
        ),
    ]
