from django.contrib import admin

# Register your models here.
from .models import Site

@admin.register(Site)
class DailyReportAdmin(admin.ModelAdmin):
    list_display = ("ba", "oa", "district", "village_site", "at3_date" )