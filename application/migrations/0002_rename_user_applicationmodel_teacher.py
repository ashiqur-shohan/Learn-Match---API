# Generated by Django 5.0.1 on 2024-03-20 04:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='applicationmodel',
            old_name='user',
            new_name='teacher',
        ),
    ]
