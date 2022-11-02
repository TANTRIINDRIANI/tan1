from django.contrib import admin
from Mahasiswa.models import MAHASISWA, FAKULTAS, prodi
# Register your models here.

class MahasiswaAdmin(admin.ModelAdmin):
    list_display = ['No', 'NIM', 'Nama', 'TTL', 'Alamat', 'Fakultas', 'Prodi', 'Email', 'Foto']
    search_fields = ['NIM', 'Nama', 'Fakultas', 'Prodi']
    list_filter = ('Fakultas_id',)
    list_per_page = 4
    
admin.site.register(MAHASISWA)
admin.site.register(FAKULTAS)
admin.site.register(prodi)