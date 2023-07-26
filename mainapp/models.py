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










    number_azs = models.CharField(max_length=50, verbose_name='Номер АЗС')


    DT = models.CharField(max_length=20, verbose_name='ДТ', blank=True, null=True)
    DT_Taneko = models.CharField(max_length=20, verbose_name='ДТ_танеко', blank=True, null=True)
    DT_winter = models.CharField(max_length=20, verbose_name='ДТ_зимнее', blank=True, null=True)
    DT_arctic = models.CharField(max_length=20, verbose_name='ДТ_арктика', blank=True, null=True)
