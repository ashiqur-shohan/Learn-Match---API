# Generated by Django 5.0.1 on 2024-03-18 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TuitionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(choices=[('EIGHT', 'EIGHT'), ('NINE', 'NINE'), ('SSC', 'SSC'), ('HSC', 'HSC'), ('ADMISION', 'ADMISION')], max_length=12)),
                ('grade_slug', models.SlugField(max_length=12)),
                ('tuition_type', models.CharField(choices=[('ONLINE', 'ONLINE'), ('OFFLINE', 'OFFLINE')], max_length=12)),
                ('salary', models.IntegerField()),
                ('location', models.CharField(max_length=30)),
                ('location_slug', models.SlugField(max_length=30)),
                ('day_perweek', models.CharField(choices=[(3, 3), (4, 4), (5, 5), (6, 6)], max_length=10)),
                ('available', models.BooleanField(default=False)),
            ],
        ),
    ]
