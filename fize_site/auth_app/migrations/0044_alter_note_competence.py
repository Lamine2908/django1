# Generated by Django 5.0.7 on 2024-09-17 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0043_alter_note_competence'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='competence',
            field=models.TextField(max_length=10),
        ),
    ]