# Generated by Django 3.2.1 on 2021-09-06 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myportfolio', '0003_workexperience_workskill'),
    ]

    operations = [
        migrations.AddField(
            model_name='prospect',
            name='company',
            field=models.CharField(default='none', max_length=144),
        ),
    ]