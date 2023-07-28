from django.contrib import admin
from .models import *
# Register your models here.
from import_export.fields import Field

from import_export.admin import ImportExportActionModelAdmin
from import_export import fields, resources



class CityResource(resources.ModelResource):

    город = Field(attribute='xxx', column_name='xxx')

    class Meta:
        model = City
        skip_unchanged = True




class CityAdmin(ImportExportActionModelAdmin):
    list_display = ('id', 'город')
    list_display_links = ('id', 'город')

admin.site.register(City, CityAdmin)