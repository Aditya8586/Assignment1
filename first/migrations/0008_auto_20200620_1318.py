# Generated by Django 2.2.2 on 2020-06-20 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0007_active_online'),
    ]

    operations = [
        migrations.AlterField(
            model_name='active',
            name='online',
            field=models.BinaryField(default=0),
        ),
    ]
