# Generated by Django 5.0.1 on 2024-04-10 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_remove_teachermodel_image_teacherimagemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='teachermodel',
            name='image',
            field=models.ImageField(null=True, upload_to='user/images'),
        ),
    ]
