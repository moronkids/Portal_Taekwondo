# Generated by Django 2.1 on 2019-03-30 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zwinkle', '0014_auto_20190330_1238'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='gambar',
            field=models.FileField(null=True, upload_to='images'),
        ),
    ]
