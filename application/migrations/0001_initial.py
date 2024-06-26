# Generated by Django 5.0.1 on 2024-03-18 15:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tuition', '0003_alter_tuitionmodel_day_perweek'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confirm', models.BooleanField(default=False)),
                ('tuition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tuition.tuitionmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.teachermodel')),
            ],
        ),
    ]
