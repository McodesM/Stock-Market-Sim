# Generated by Django 4.2.6 on 2024-03-19 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('broker', '0017_remove_simuser_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='simuser',
            name='level',
            field=models.CharField(default='Novice', max_length=255),
        ),
    ]
