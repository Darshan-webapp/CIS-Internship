# Generated by Django 4.2.5 on 2023-09-25 06:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='Contacts',
            new_name='Contact',
        ),
    ]
