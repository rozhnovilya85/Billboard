from django.contrib import admin
from import_export.resources import ModelResource
from import_export.widgets import ForeignKeyWidget, DateWidget

from .models import *
# Register your models here.
from import_export.fields import Field

from import_export.admin import ImportExportActionModelAdmin, ImportExportModelAdmin
from import_export import fields, resources, widgets


class CityResource(resources.ModelResource):
    city = fields.Field(attribute='city', column_name='Город')

    class Meta:
        model = City
        skip_unchanged = True
        report_skipped = True
        # exclude = ('id', 'city',)
        import_id_fields = ('city',)
        # fields = ('id', 'city',)


class CityAdmin(ImportExportModelAdmin):
    resource_class = CityResource
    list_display = ('id', 'city')
    list_display_links = ('id', 'city')


admin.site.register(City, CityAdmin)


class SurfaceTypeResource(resources.ModelResource):
    surface_type = fields.Field(attribute='surface_type', column_name='Тип поверхности')

    class Meta:
        model = Surface_type
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('surface_type',)


class SurfaceTypeAdmin(ImportExportModelAdmin):
    resource_class = SurfaceTypeResource
    list_display = ('id', 'surface_type')
    list_display_links = ('id', 'surface_type')

admin.site.register(Surface_type, SurfaceTypeAdmin)

class IlluminationResource(resources.ModelResource):
    illumination = fields.Field(attribute='illumination', column_name='Осв')

    class Meta:
        model = Illumination
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('illumination',)


class IlluminationAdmin(ImportExportModelAdmin):
    resource_class = IlluminationResource
    list_display = ('id', 'illumination')
    list_display_links = ('id', 'illumination')

admin.site.register(Illumination, IlluminationAdmin)


class SideResource(resources.ModelResource):
    side = fields.Field(attribute='side', column_name='Сторона')

    class Meta:
        model = Side
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('side',)


class SideAdmin(ImportExportModelAdmin):
    resource_class = SideResource
    list_display = ('id', 'side')
    list_display_links = ('id', 'side')

admin.site.register(Side, SideAdmin)


class MediaMaterialResource(resources.ModelResource):
    media_material = fields.Field(attribute='media_material', column_name='Материал носителя')

    class Meta:
        model = Media_material
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('media_material',)


class MediaMaterialAdmin(ImportExportModelAdmin):
    resource_class = MediaMaterialResource
    list_display = ('id', 'media_material')
    list_display_links = ('id', 'media_material')

admin.site.register(Media_material, MediaMaterialAdmin)

class CityDistrictResource(resources.ModelResource):
    city_district = fields.Field(attribute='city_district', column_name='Городской Округ')

    class Meta:
        model = City_district
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('city_district',)


class CityDistrictAdmin(ImportExportModelAdmin):
    resource_class = CityDistrictResource
    list_display = ('id', 'city_district')
    list_display_links = ('id', 'city_district')

admin.site.register(City_district, CityDistrictAdmin)


class SalesResource(resources.ModelResource):
    internal_code = fields.Field(attribute='internal_code', column_name='Вн. код')
    july_2023 = fields.Field(attribute='july_2023', column_name='Июль 2023')
    august_2023 = fields.Field(attribute='august_2023', column_name='Август 2023')
    september_2023 = fields.Field(attribute='september_2023', column_name='Сентябрь 2023')
    october_2023 = fields.Field(attribute='october_2023', column_name='Октябрь 2023')
    november_2023 = fields.Field(attribute='november_2023', column_name='Ноябрь 2023')
    december_2023 = fields.Field(attribute='december_2023', column_name='Декабрь 2023')

    class Meta:
        model = Sales
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('internal_code',)


class SalesAdmin(ImportExportModelAdmin):
    resource_class = SalesResource
    list_display = ('id', 'internal_code', 'july_2023', 'august_2023', 'september_2023', 'october_2023', 'november_2023', 'december_2023')
    list_display_links = ('id', 'internal_code')


admin.site.register(Sales, SalesAdmin)


class BillboardDBResource(resources.ModelResource):
    internal_code = fields.Field(attribute='internal_code', column_name='Вн. код')
    address = fields.Field(attribute='address', column_name='Адрес')
    city = fields.Field(attribute='city', column_name='Город', widget=ForeignKeyWidget(City, 'city'))
    surface_type = fields.Field(attribute='surface_type', column_name='Тип поверхности', widget=ForeignKeyWidget(Surface_type, 'surface_type'))
    illumination = fields.Field(attribute='illumination', column_name='Осв', widget=ForeignKeyWidget(Illumination, 'illumination'))
    side = fields.Field(attribute='side', column_name='Сторона', widget=ForeignKeyWidget(Side, 'side'))
    latitude = fields.Field(attribute='latitude', column_name='Широта')
    longitude = fields.Field(attribute='longitude', column_name='Долгота')
    photo = fields.Field(attribute='photo', column_name='фото/схема')
    price = fields.Field(attribute='price', column_name='Прайс C НДС', widget=widgets.FloatWidget())
    digital_quantity = fields.Field(attribute='digital_quantity', column_name='Диджтал кол-во показов', widget=widgets.FloatWidget())
    grp = fields.Field(attribute='grp', column_name='GRP', widget=widgets.FloatWidget())
    ots = fields.Field(attribute='ots', column_name='OTS', widget=widgets.FloatWidget())
    code_espar = fields.Field(attribute='code_espar', column_name='Код Эспар')
    media_material = fields.Field(attribute='media_material', column_name='Материал носителя', widget=ForeignKeyWidget(Media_material, 'media_material'))
    product_restrictions = fields.Field(attribute='product_restrictions', column_name='Ограничения по продукту')
    city_district = fields.Field(attribute='city_district', column_name='Городской Округ', widget=ForeignKeyWidget(City_district, 'city_district'))
    Technical_requirements = fields.Field(attribute='Technical_requirements', column_name='Тех. требования')
    price_montage = fields.Field(attribute='price_montage', column_name='Монтаж. Прайс  с НДС', widget=widgets.FloatWidget())
    price_plywood = fields.Field(attribute='price_plywood', column_name='Переклейка. Прайс с НДС', widget=widgets.FloatWidget())
    permission = fields.Field(attribute='permission', column_name='Разрешение ПО', widget=DateWidget(format='%d.%m.%Y'))
    note = fields.Field(attribute='note', column_name='Примечание')
    sales = fields.Field(attribute='sales', column_name='Вн. код', widget=ForeignKeyWidget(Sales, 'internal_code'))

    class Meta:
        model = BillboardDB
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('internal_code',)


class BillboardDBAdmin(ImportExportModelAdmin):
    resource_class = BillboardDBResource
    list_display = ('id', 'internal_code', 'address', 'city', 'surface_type', 'illumination', 'side', 'latitude', 'longitude',
    'photo',
    'price', 'digital_quantity', 'grp', 'ots', 'code_espar', 'media_material', 'product_restrictions', 'city_district',
    'Technical_requirements', 'price_montage', 'price_plywood', 'permission', 'note', 'sales')

    list_display_links = ('id', 'internal_code')

admin.site.register(BillboardDB, BillboardDBAdmin)
