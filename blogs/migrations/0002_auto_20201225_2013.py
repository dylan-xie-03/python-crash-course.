# Generated by Django 3.1.4 on 2020-12-25 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='date_add',
            new_name='date_added',
        ),
    ]
