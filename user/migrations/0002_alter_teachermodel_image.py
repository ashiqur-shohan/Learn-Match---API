# Generated by Django 5.0.1 on 2024-03-23 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachermodel',
            name='image',
            field=models.ImageField(null=True, upload_to='user/images'),
        ),
    ]