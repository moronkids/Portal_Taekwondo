# Generated by Django 2.1 on 2019-01-14 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zwinkle', '0036_auto_20190114_0742'),
    ]

    operations = [
        migrations.CreateModel(
            name='foto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='documents')),
            ],
        ),
    ]