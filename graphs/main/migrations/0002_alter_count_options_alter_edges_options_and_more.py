# Generated by Django 5.0 on 2023-12-06 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='count',
            options={'verbose_name': 'Количество', 'verbose_name_plural': 'Количество'},
        ),
        migrations.AlterModelOptions(
            name='edges',
            options={'verbose_name': 'Ребро', 'verbose_name_plural': 'Ребра'},
        ),
        migrations.AlterModelOptions(
            name='names',
            options={'verbose_name': 'Название', 'verbose_name_plural': 'Названия'},
        ),
        migrations.AlterField(
            model_name='count',
            name='count',
            field=models.CharField(max_length=10, verbose_name='Количество'),
        ),
    ]
