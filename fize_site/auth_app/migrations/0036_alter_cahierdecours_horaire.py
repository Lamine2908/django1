# Generated by Django 5.0.7 on 2024-09-13 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0035_alter_cahierdecours_horaire'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cahierdecours',
            name='horaire',
            field=models.CharField(max_length=20),
        ),
    ]