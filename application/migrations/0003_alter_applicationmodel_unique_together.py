# Generated by Django 5.0.1 on 2024-04-11 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_rename_user_applicationmodel_teacher'),
        ('tuition', '0005_alter_tuitionmodel_day_perweek'),
        ('user', '0013_remove_teachermodel_image'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='applicationmodel',
            unique_together={('teacher', 'tuition')},
        ),
    ]
