# Generated by Django 2.2.4 on 2019-10-21 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_auto_20191021_1807'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='complevel',
            options={'verbose_name': '赛事等级', 'verbose_name_plural': '赛事等级表'},
        ),
        migrations.AlterModelOptions(
            name='markmessage',
            options={'verbose_name': '收藏记录', 'verbose_name_plural': '收藏列表'},
        ),
        migrations.AlterModelTable(
            name='complevel',
            table='CompLevel',
        ),
        migrations.AlterModelTable(
            name='markmessage',
            table='MarkMessage',
        ),
    ]
