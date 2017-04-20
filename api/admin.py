from django.contrib import admin
from django.contrib.admin import AdminSite
from api.models import Trail


class HikeOregonAdminSite(AdminSite):
    site_header = 'Hike Oregon administration'


class TrailAdmin(admin.ModelAdmin):
    pass

admin_site = HikeOregonAdminSite(name='HikeOregon')
admin_site.register(Trail, TrailAdmin)
