# Generated by Django 4.0.2 on 2022-08-06 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0002_word'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='pronunciation',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='word',
            name='score',
            field=models.FloatField(default=0.0),
        ),
    ]