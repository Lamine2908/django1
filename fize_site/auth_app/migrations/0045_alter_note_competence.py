# Generated by Django 5.0.7 on 2024-09-17 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0044_alter_note_competence'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='competence',
            field=models.CharField(max_length=10),
        ),
    ]