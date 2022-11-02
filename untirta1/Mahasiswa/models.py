from pickle import TRUE
from django.db import models

# Create your models here.
class FAKULTAS(models.Model):
    id_FAKULTAS = models.CharField(max_length=9)
    nama = models.CharField(max_length=9)

class prodi(models.Model):
    id_Prodi = models.CharField(max_length=9)
    nama = models.CharField(max_length=9)
    
class MAHASISWA(models.Model):
    NIM=models.CharField(max_length=50)
    NAMA=models.CharField(max_length=40)
    TTL=models.CharField(max_length=40)
    PHOTO=models.CharField(max_length=40)
    EMAIL=models.CharField(max_length=40)
    FAKULTAS_id = models.ForeignKey(FAKULTAS, on_delete=models.CASCADE, null=True)
    PRODI_id = models.ForeignKey(prodi, on_delete=models.CASCADE, null=True)

    def _str_(self):
        return self.NIM

