# Generated by Django 5.0.1 on 2024-04-29 04:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vote_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Qusetion',
            new_name='Question',
        ),
    ]