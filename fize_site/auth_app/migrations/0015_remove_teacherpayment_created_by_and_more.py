# Generated by Django 5.0.7 on 2024-09-10 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0014_teacherpayment_delete_paiementteacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacherpayment',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='teacherpayment',
            name='payment_date',
        ),
        migrations.AddField(
            model_name='teacherpayment',
            name='payment_method',
            field=models.CharField(choices=[('wave', 'Wave'), ('orange_money', 'Orange Money'), ('other', 'Autre')], default='other', max_length=20),
        ),
        migrations.AlterField(
            model_name='teacherpayment',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]