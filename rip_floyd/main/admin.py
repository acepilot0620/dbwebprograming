from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *


@admin.register(Police_victim,Victims)
class InfluencerAdmin(ImportExportModelAdmin):
    pass
