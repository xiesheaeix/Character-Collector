# Generated by Django 4.1.3 on 2022-11-17 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_remove_award_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='awards',
            field=models.ManyToManyField(to='main_app.award'),
        ),
    ]
