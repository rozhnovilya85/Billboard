from django.contrib import admin
from .models import *
# Register your models here.
from import_export.fields import Field

from import_export.admin import ImportExportActionModelAdmin
from import_export import fields, resources



class CityResource(resources.ModelResource):

    city = Field(attribute='city', column_name='city')

    class Meta:
        model = City
        skip_unchanged = True
        import_id_fields = ('city',)
        fields = ('id', 'city',)




class CityAdmin(ImportExportActionModelAdmin):
    list_display = ('id', 'city')
    list_display_links = ('id', 'city')

admin.site.register(City, CityAdmin)