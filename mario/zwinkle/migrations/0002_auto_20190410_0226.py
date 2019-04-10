# Generated by Django 2.1 on 2019-04-10 02:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zwinkle', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collection',
            old_name='ttl',
            new_name='tempat_lahir',
        ),
        migrations.AddField(
            model_name='collection',
            name='tanggal_lahir',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
