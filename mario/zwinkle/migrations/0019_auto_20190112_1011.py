# Generated by Django 2.1 on 2019-01-12 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zwinkle', '0018_auto_20190112_1008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='krida_model',
            name='hasilujian',
            field=models.CharField(choices=[('LULUS', 'LULUS'), ('TIDAK LULUS', 'TIDAK LULUS'), ('-', '-')], default=1, max_length=100),
        ),
    ]
