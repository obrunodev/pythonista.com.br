# Generated by Django 4.2.17 on 2024-12-20 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['status', 'due_date'], 'verbose_name': 'Tarefa', 'verbose_name_plural': 'Tarefas'},
        ),
    ]