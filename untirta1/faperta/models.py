from pickle import TRUE
from django.db import models

# Create your models here.
class STAFF(models.Model):
    NIP=models.CharField(max_length=50)
    NAMA=models.CharField(max_length=40)
    TTL=models.CharField(max_length=40)
    PHOTO=models.CharField(max_length=40)
    EMAIL=models.CharField(max_length=40)
    UNIT=models.CharField(max_length=40)
    ALAMAT=models.CharField(max_length=40)

    def _str_(self):
        return self.NIP

class MAHASISWA(models.Model):
    NIM=models.CharField(max_length=50)
    NAMA=models.CharField(max_length=40)
    TTL=models.CharField(max_length=40)
    PHOTO=models.CharField(max_length=40)
    EMAIL=models.CharField(max_length=40)
    FAKULTAS=models.CharField(max_length=40)
    PRODI=models.CharField(max_length=40)

    def _str_(self):
        return self.NIP

class DOSEN(models.Model):
    NIM=models.CharField(max_length=50)
    NAMA=models.CharField(max_length=40)
    TTL=models.CharField(max_length=40)
    PHOTO=models.CharField(max_length=40)
    EMAIL=models.CharField(max_length=40)
    FAKULTAS=models.CharField(max_length=40)
    PRODI=models.CharField(max_length=40)
    ALAMAT=models.CharField(max_length=40)
    
    

    def _str_(self):
        return self.NIP