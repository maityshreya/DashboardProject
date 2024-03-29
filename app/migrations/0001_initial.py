# Generated by Django 4.2.7 on 2023-12-19 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DashboardData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intensity', models.IntegerField()),
                ('likelihood', models.IntegerField()),
                ('relevance', models.IntegerField()),
                ('year', models.IntegerField()),
                ('country', models.CharField(max_length=255)),
                ('topics', models.CharField(max_length=255)),
                ('region', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
            ],
        ),
    ]
