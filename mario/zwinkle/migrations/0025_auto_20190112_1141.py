# Generated by Django 2.1 on 2019-01-12 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zwinkle', '0024_auto_20190112_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='model_pic',
            field=models.FileField(upload_to='media/'),
        ),
    ]