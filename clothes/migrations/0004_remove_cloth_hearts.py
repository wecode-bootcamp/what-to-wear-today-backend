# Generated by Django 2.2 on 2019-05-09 03:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0003_auto_20190508_1551'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cloth',
            name='hearts',
        ),
    ]