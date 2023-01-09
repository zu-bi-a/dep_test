# Generated by Django 4.0.2 on 2022-08-14 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0003_word_pronunciation_alter_word_score'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='word',
            name='pronunciation',
        ),
        migrations.AddField(
            model_name='word',
            name='spokenAudio',
            field=models.FileField(default='', upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='word',
            name='spokenPhonetics',
            field=models.TextField(blank=True, null=True),
        ),
    ]
