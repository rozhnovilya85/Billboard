from django.db import models

# Create your models here.


class BillboardDB(models.Model):

    internal_code = models.CharField(max_length=20, verbose_name='Вн.код')
    address = models.CharField(max_length=250, verbose_name='Адрес')
    city = models.ForeignKey('City', on_delete=models.PROTECT, null=True, verbose_name='Город')
    surface_type = models.ForeignKey('Surface_type', on_delete=models.PROTECT, null=True, verbose_name='Тип поверхности')
    illumination = models.ForeignKey('Illumination', on_delete=models.PROTECT, null=True, verbose_name='Осв')
    side = models.ForeignKey('Side', on_delete=models.PROTECT, null=True, verbose_name='Сторона')
    latitude = models.DecimalField(max_digits=12, decimal_places=10, verbose_name='Широта')
    longitude = models.DecimalField(max_digits=12, decimal_places=10, verbose_name='Долгота')
    photo = models.CharField(max_length=250, verbose_name='фото/схема')
    price = models.FloatField(blank=True, null=True, verbose_name='Прайс с НДС')
    digital_quantity = models.FloatField(blank=True, null=True, verbose_name='Диджтал кол-во показов')
    grp = models.FloatField(blank=True, null=True, verbose_name='GRP')
    ots = models.FloatField(blank=True, null=True, verbose_name='OTS')
    code_espar = models.CharField(max_length=50,blank=True, null=True, verbose_name='Код Эспар')
    media_material = models.ForeignKey('Media_material', on_delete=models.PROTECT, null=True, verbose_name='Материал носителя')
    product_restrictions = models.CharField(max_length=250, verbose_name='Ограничения по продукту')
    city_district = models.ForeignKey('City_district', on_delete=models.PROTECT, null=True, verbose_name='Городской округ')
    Technical_requirements = models.CharField(max_length=250, verbose_name='Тех.требования')
    price_montage = models.FloatField(blank=True, null=True, verbose_name='Монтаж. Прайс с НДС')
    price_plywood = models.FloatField(blank=True, null=True, verbose_name='Переклейка. Прайс с НДС')
    permission = models.DateField(null=True, verbose_name='Разрешение ПО')
    note = models.CharField(max_length=250, verbose_name='Примечание')
    sales = models.OneToOneField('Sales', on_delete=models.PROTECT, null=True, verbose_name='Продажи')

    def __str__(self):  # Переопределение названия объекта
        return self.internal_code

    class Meta:  # Класс для названий нашей модели в админке
        verbose_name = 'Билборд'  # Надпись в единственном числе
        verbose_name_plural = 'Билборды'  # Надпись во множественном числе
        ordering = ['internal_code']  # Сортировка полей (по возрастанию)


class City(models.Model):

    city = models.CharField(max_length=30, verbose_name='Город')

    def __str__(self):  # Переопределение названия объекта
        return self.city

    class Meta:  # Класс для названий нашей модели в админке
        verbose_name = 'Город'  # Надпись в единственном числе
        verbose_name_plural = 'Города'  # Надпись во множественном числе
        ordering = ['city']  # Сортировка полей (по возрастанию)


class Surface_type(models.Model):

    surface_type = models.CharField(max_length=150, unique=True, verbose_name='Тип поверхности')

    def __str__(self):  # Переопределение названия объекта
        return self.surface_type


class Illumination(models.Model):

    illumination = models.CharField(max_length=30, unique=True, verbose_name='Осв')

    def __str__(self):  # Переопределение названия объекта
        return self.illumination


class Side(models.Model):

    side = models.CharField(max_length=30, unique=True, verbose_name='Сторона')

    def __str__(self):  # Переопределение названия объекта
        return self.side


class Media_material(models.Model):

    media_material = models.CharField(max_length=150, unique=True, verbose_name='Материал носителя')

    def __str__(self):  # Переопределение названия объекта
        return self.media_material


class City_district(models.Model):
    city_district = models.CharField(max_length=150, unique=True, verbose_name='Городской округ')

    def __str__(self):  # Переопределение названия объекта
        return self.city_district


class Sales(models.Model):
    internal_code = models.CharField(max_length=20, verbose_name='Вн.код')
    july_2023 = models.CharField(max_length=250, verbose_name='Июль 2023')
    august_2023 = models.CharField(max_length=250, verbose_name='Агуст 2023')
    september_2023 = models.CharField(max_length=250, verbose_name='Сентябрь 2023')
    october_2023 = models.CharField(max_length=250, verbose_name='Октябрь 2023')
    november_2023 = models.CharField(max_length=250, verbose_name='Ноябрь 2023')
    december_2023 = models.CharField(max_length=250, verbose_name='Декабрь 2023')

    def __str__(self):  # Переопределение названия объекта
        return self.internal_code









