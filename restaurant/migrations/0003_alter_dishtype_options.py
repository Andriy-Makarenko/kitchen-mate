# Generated by Django 4.1 on 2022-11-10 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_alter_dish_options_alter_dishtype_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dishtype',
            options={'ordering': ['name'], 'verbose_name': 'dish type', 'verbose_name_plural': 'dishes types'},
        ),
    ]
