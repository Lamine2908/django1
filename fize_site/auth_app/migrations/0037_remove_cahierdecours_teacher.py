# Generated by Django 5.0.7 on 2024-09-15 04:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0036_alter_cahierdecours_horaire'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cahierdecours',
            name='teacher',
        ),
    ]
