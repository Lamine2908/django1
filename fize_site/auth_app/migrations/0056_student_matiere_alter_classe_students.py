# Generated by Django 5.0.7 on 2024-09-27 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0055_classe_filiere_matiere_filiere'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='matiere',
            field=models.ManyToManyField(related_name='students', to='auth_app.matiere'),
        ),
        migrations.AlterField(
            model_name='classe',
            name='students',
            field=models.ManyToManyField(related_name='classes', to='auth_app.student'),
        ),
    ]
