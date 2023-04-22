# Generated by Django 4.1.7 on 2023-04-13 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_alter_periodsownership_before_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=200, verbose_name='Марка')),
                ('model', models.CharField(max_length=200, verbose_name='Модель')),
                ('year', models.PositiveSmallIntegerField(verbose_name='Год выпуска')),
                ('color', models.CharField(max_length=100, verbose_name='Цвет')),
                ('rudder_location', models.CharField(max_length=100, verbose_name='Расположение руля')),
                ('engine_volume', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Объем двигателя')),
                ('price', models.PositiveIntegerField(blank=True, null=True, verbose_name='Цена')),
                ('mileage', models.PositiveIntegerField(blank=True, null=True, verbose_name='Пробег')),
                ('transmission', models.CharField(blank=True, max_length=100, null=True, verbose_name='Коробка передач')),
                ('region', models.CharField(blank=True, max_length=255, null=True, verbose_name='Регион')),
                ('accounting', models.CharField(blank=True, max_length=200, null=True, verbose_name='Учёт')),
                ('another', models.CharField(max_length=500, verbose_name='Прочее')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
            },
        ),
    ]