# Generated by Django 2.1 on 2019-01-14 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zwinkle', '0040_auto_20190114_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='gambar',
            field=models.ImageField(default='media/images/vespa.jpg', upload_to='images'),
        ),
    ]
