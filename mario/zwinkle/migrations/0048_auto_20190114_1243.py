# Generated by Django 2.1 on 2019-01-14 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zwinkle', '0047_auto_20190114_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='gambar',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
