# Generated by Django 2.1 on 2019-04-10 02:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zwinkle', '0004_auto_20190410_0255'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collection',
            name='umur',
        ),
    ]
