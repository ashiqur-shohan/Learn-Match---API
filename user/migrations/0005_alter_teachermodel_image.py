# Generated by Django 5.0.1 on 2024-04-08 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_teachermodel_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachermodel',
            name='image',
            field=models.ImageField(null=True, upload_to='media/user/images'),
        ),
    ]
