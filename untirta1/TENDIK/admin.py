from django.contrib import admin
from TENDIK.models import STAFF
# Register your models here.
class TENDIKAdmin(admin.ModelAdmin):
    list_display = ['No', 'NIP', 'Nama', 'TTL', 'Alamat', 'unit', 'Email', 'Foto']
    search_fields = ['NIP', 'Nama', 'Unit']
    list_filter = ('No',)
    list_per_page = 4
admin.site.register(STAFF)