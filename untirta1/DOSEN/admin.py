from django.contrib import admin
from DOSEN.models import DOSEN, FAKULTAS, prodi
# Register your models here.

class DOSENAdmin(admin.ModelAdmin):
    list_display = ['No', 'NIP', 'Nama', 'TTL', 'Alamat', 'Fakultas', 'Prodi', 'Email', 'Foto']
    search_fields = ['NIP', 'Nama', 'Fakultas', 'Prodi']
    list_filter = ('Fakultas_id',)
    list_per_page = 4
admin.site.register(DOSEN)
admin.site.register(FAKULTAS)
admin.site.register(prodi)
