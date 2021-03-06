# Generated by Django 3.2.1 on 2021-09-06 00:49

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myportfolio', '0002_auto_20210905_1749'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=144)),
                ('title', models.CharField(max_length=144)),
                ('start_year', models.DateField(default=datetime.datetime(1900, 1, 1, 0, 0))),
                ('end_year', models.DateField(default=datetime.datetime(1900, 1, 1, 0, 0))),
                ('is_current', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='WorkSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Skill', max_length=1024)),
                ('job', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myportfolio.workexperience')),
            ],
        ),
    ]
