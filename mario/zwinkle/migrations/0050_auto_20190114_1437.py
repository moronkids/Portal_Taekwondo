# Generated by Django 2.1 on 2019-01-14 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zwinkle', '0049_auto_20190114_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='gambar',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
