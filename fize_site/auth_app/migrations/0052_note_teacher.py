# Generated by Django 5.0.7 on 2024-09-20 04:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0051_alter_note_appreciation_alter_note_competence_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth_app.teacher'),
        ),
    ]
