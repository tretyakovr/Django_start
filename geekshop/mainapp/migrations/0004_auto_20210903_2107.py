# Generated by Django 3.2.6 on 2021-09-03 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20210903_0726'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Наименование')),
                ('comments', models.TextField(blank=True, verbose_name='Примечание')),
            ],
            options={
                'verbose_name': 'Категории товаров',
                'db_table': 'Category',
            },
        ),
        migrations.AlterModelOptions(
            name='params',
            options={'verbose_name': 'Параметры'},
        ),
        migrations.AddField(
            model_name='products',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.RESTRICT, to='mainapp.category'),
            preserve_default=False,
        ),
    ]
