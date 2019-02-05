# Generated by Django 2.1 on 2019-01-10 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zwinkle', '0009_krida_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='copy_krida_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=30, unique=True)),
                ('umur', models.CharField(max_length=30)),
                ('penguji', models.CharField(max_length=30)),
                ('sabuk', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='krida_model',
            name='nama',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
