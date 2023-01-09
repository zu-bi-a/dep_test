# Generated by Django 4.0.2 on 2022-08-15 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0005_word_correctaudio_word_correctphonetics_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='correctAudio',
            field=models.FileField(blank=True, default='s', upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='word',
            name='correctPhonetics',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='word',
            name='spokenPhonetics',
            field=models.TextField(blank=True),
        ),
    ]