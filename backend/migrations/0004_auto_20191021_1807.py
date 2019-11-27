# Generated by Django 2.2.4 on 2019-10-21 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_auto_20191014_1438'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='area',
            options={'verbose_name': '地区', 'verbose_name_plural': '地区列表'},
        ),
        migrations.AlterModelOptions(
            name='bbsreply',
            options={'verbose_name': '回复信息', 'verbose_name_plural': '回复信息列表'},
        ),
        migrations.AlterModelOptions(
            name='bbssection',
            options={'verbose_name': '板块信息', 'verbose_name_plural': '板块列表'},
        ),
        migrations.AlterModelOptions(
            name='bbstopic',
            options={'verbose_name': '主贴信息', 'verbose_name_plural': '主帖列表'},
        ),
        migrations.AlterModelOptions(
            name='compclass',
            options={'verbose_name': '赛事类别', 'verbose_name_plural': '赛事类别列表'},
        ),
        migrations.AlterModelOptions(
            name='compinfo',
            options={'verbose_name': '赛事信息', 'verbose_name_plural': '赛事列表'},
        ),
        migrations.AlterModelOptions(
            name='comprecord',
            options={'verbose_name': '赛事记录', 'verbose_name_plural': '赛事记录列表'},
        ),
        migrations.AlterModelOptions(
            name='usermessage',
            options={'verbose_name': '用户信息', 'verbose_name_plural': '用户列表'},
        ),
        migrations.AlterModelTable(
            name='area',
            table='Area',
        ),
        migrations.AlterModelTable(
            name='bbsreply',
            table='BBSReply',
        ),
        migrations.AlterModelTable(
            name='bbssection',
            table='BBSSection',
        ),
        migrations.AlterModelTable(
            name='bbstopic',
            table='BBSTopic',
        ),
        migrations.AlterModelTable(
            name='compclass',
            table='CompClass',
        ),
        migrations.AlterModelTable(
            name='compinfo',
            table='CompInfo',
        ),
        migrations.AlterModelTable(
            name='comprecord',
            table='CompRecord',
        ),
        migrations.AlterModelTable(
            name='usermessage',
            table='Users',
        ),
    ]
