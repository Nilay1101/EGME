# Generated by Django 3.0 on 2019-12-21 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0017_auto_20191221_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additem',
            name='pic',
            field=models.ImageField(upload_to=''),
        ),
    ]
