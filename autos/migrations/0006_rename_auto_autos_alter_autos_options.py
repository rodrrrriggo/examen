# Generated by Django 4.1.2 on 2024-06-29 01:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autos', '0005_alter_auto_imagen'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Auto',
            new_name='Autos',
        ),
        migrations.AlterModelOptions(
            name='autos',
            options={'verbose_name': 'auto', 'verbose_name_plural': 'auto'},
        ),
    ]
