# Generated by Django 5.0.7 on 2024-09-13 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0034_delete_evaluation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cahierdecours',
            name='horaire',
            field=models.CharField(max_length=10),
        ),
    ]
