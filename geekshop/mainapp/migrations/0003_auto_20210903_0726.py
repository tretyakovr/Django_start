# Generated by Django 3.2.6 on 2021-09-03 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20210903_0708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='params',
            name='comments',
            field=models.TextField(blank=True, verbose_name='Примечание'),
        ),
        migrations.AlterField(
            model_name='prodparams',
            name='comments',
            field=models.TextField(blank=True, verbose_name='Примечание'),
        ),
        migrations.AlterField(
            model_name='products',
            name='comments',
            field=models.TextField(blank=True, verbose_name='Примечание'),
        ),
    ]
