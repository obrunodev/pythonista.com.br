# Generated by Django 4.2.17 on 2025-01-26 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0003_transaction_is_permanent_debt_transaction_debt'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='is_paid',
            field=models.BooleanField(default=False, verbose_name='Está pago?'),
        ),
    ]
