# Generated by Django 3.2.14 on 2022-07-28 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_appointment_pat'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='pat',
            new_name='pat1',
        ),
    ]
