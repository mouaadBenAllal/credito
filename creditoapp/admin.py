from django.contrib import admin
from .models import Werknemer
# Register your models here.


class WerknemerAdmin(admin.ModelAdmin):
    list_display = ['id', 'organisatie', 'voornaam', 'tussenvoegsel', 'achternaam', 'email', 'rol']
    search_fields = ['voornaam']

admin.site.register(Werknemer, WerknemerAdmin)