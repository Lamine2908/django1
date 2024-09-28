# Generated by Django 5.0.7 on 2024-09-09 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0003_delete_adjointclasse'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdjointClasse',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
            ],
        ),
    ]
