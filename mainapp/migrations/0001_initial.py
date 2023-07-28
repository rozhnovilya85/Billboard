# Generated by Django 4.2.3 on 2023-07-28 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=30, unique=True, verbose_name='Город')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
                'ordering': ['city'],
            },
        ),
        migrations.CreateModel(
            name='City_district',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_district', models.CharField(max_length=150, unique=True, verbose_name='Городской округ')),
            ],
        ),
        migrations.CreateModel(
            name='Illumination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('illumination', models.CharField(max_length=30, unique=True, verbose_name='Осв')),
            ],
        ),
        migrations.CreateModel(
            name='Media_material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media_material', models.CharField(max_length=150, unique=True, verbose_name='Материал носителя')),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('internal_code', models.CharField(max_length=20, verbose_name='Вн.код')),
                ('july_2023', models.CharField(max_length=250, verbose_name='Июль 2023')),
                ('august_2023', models.CharField(max_length=250, verbose_name='Агуст 2023')),
                ('september_2023', models.CharField(max_length=250, verbose_name='Сентябрь 2023')),
                ('october_2023', models.CharField(max_length=250, verbose_name='Октябрь 2023')),
                ('november_2023', models.CharField(max_length=250, verbose_name='Ноябрь 2023')),
                ('december_2023', models.CharField(max_length=250, verbose_name='Декабрь 2023')),
            ],
        ),
        migrations.CreateModel(
            name='Side',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('side', models.CharField(max_length=30, unique=True, verbose_name='Сторона')),
            ],
        ),
        migrations.CreateModel(
            name='Surface_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surface_type', models.CharField(max_length=150, unique=True, verbose_name='Тип поверхности')),
            ],
        ),
        migrations.CreateModel(
            name='BillboardDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('internal_code', models.CharField(max_length=20, verbose_name='Вн.код')),
                ('address', models.CharField(max_length=250, verbose_name='Адрес')),
                ('latitude', models.DecimalField(decimal_places=10, max_digits=12, verbose_name='Широта')),
                ('longitude', models.DecimalField(decimal_places=10, max_digits=12, verbose_name='Долгота')),
                ('photo', models.CharField(max_length=250, verbose_name='фото/схема')),
                ('price', models.FloatField(blank=True, null=True, verbose_name='Прайс с НДС')),
                ('digital_quantity', models.FloatField(blank=True, null=True, verbose_name='Диджтал кол-во показов')),
                ('grp', models.FloatField(blank=True, null=True, verbose_name='GRP')),
                ('ots', models.FloatField(blank=True, null=True, verbose_name='OTS')),
                ('code_espar', models.CharField(blank=True, max_length=50, null=True, verbose_name='Код Эспар')),
                ('product_restrictions', models.CharField(max_length=250, verbose_name='Ограничения по продукту')),
                ('Technical_requirements', models.CharField(max_length=250, verbose_name='Тех.требования')),
                ('price_montage', models.FloatField(blank=True, null=True, verbose_name='Монтаж. Прайс с НДС')),
                ('price_plywood', models.FloatField(blank=True, null=True, verbose_name='Переклейка. Прайс с НДС')),
                ('permission', models.DateField(null=True, verbose_name='Разрешение ПО')),
                ('note', models.CharField(max_length=250, verbose_name='Примечание')),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='mainapp.city', verbose_name='Город')),
                ('city_district', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='mainapp.city_district', verbose_name='Городской округ')),
                ('illumination', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='mainapp.illumination', verbose_name='Осв')),
                ('media_material', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='mainapp.media_material', verbose_name='Материал носителя')),
                ('sales', models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='mainapp.sales', verbose_name='Продажи')),
                ('side', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='mainapp.side', verbose_name='Сторона')),
                ('surface_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='mainapp.surface_type', verbose_name='Тип поверхности')),
            ],
            options={
                'verbose_name': 'Билборд',
                'verbose_name_plural': 'Билборды',
                'ordering': ['internal_code'],
            },
        ),
    ]
