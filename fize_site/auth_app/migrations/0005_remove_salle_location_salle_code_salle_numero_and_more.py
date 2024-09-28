# Generated by Django 5.0.7 on 2024-09-09 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0004_adjointclasse'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salle',
            name='location',
        ),
        migrations.AddField(
            model_name='salle',
            name='code',
            field=models.CharField(blank=True, max_length=10, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='salle',
            name='numero',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='salle',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
