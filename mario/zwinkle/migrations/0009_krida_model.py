# Generated by Django 2.1.4 on 2019-01-09 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zwinkle', '0008_auto_20190103_0701'),
    ]

    operations = [
        migrations.CreateModel(
            name='krida_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=30)),
                ('umur', models.CharField(max_length=30)),
                ('penguji', models.CharField(max_length=30)),
                ('sabuk', models.CharField(max_length=30)),
            ],
        ),
    ]
