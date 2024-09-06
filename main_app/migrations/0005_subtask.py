# Generated by Django 5.1 on 2024-09-05 16:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_todo_completed'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subtask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('due', models.DateField(verbose_name='Date Due')),
                ('todo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.todo')),
            ],
        ),
    ]
