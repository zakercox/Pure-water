# Generated by Django 5.0.1 on 2024-02-10 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Puer_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='fartist',
            new_name='artist',
        ),
    ]
