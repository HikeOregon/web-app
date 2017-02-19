from django.contrib import admin
from api.models import Trail

@admin.register(Trail)
class TrailAdmin(admin.ModelAdmin):
    pass
