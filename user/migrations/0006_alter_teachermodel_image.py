# Generated by Django 5.0.1 on 2024-04-08 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_teachermodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachermodel',
            name='image',
            field=models.ImageField(null=True, upload_to='user/images'),
        ),
    ]