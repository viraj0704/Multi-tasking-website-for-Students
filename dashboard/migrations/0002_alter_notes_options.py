# Generated by Django 4.0.6 on 2022-07-09 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notes',
            options={'verbose_name': 'note', 'verbose_name_plural': 'notes'},
        ),
    ]
