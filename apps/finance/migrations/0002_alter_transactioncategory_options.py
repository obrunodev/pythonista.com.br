# Generated by Django 4.2.17 on 2025-01-26 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transactioncategory',
            options={'ordering': ['category'], 'verbose_name': 'Categoria de transação', 'verbose_name_plural': 'Categorias de transação'},
        ),
    ]
