"""untirta1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Mahasiswa.views import prodiMahasiswa
from TENDIK.views import prodiTENDIK
from tirtayasa.views import proditirtayasa
from faperta.views import prodifaperta
from feb.views import prodifeb
from fh.views import prodifh
from fisip.views import prodifisip
from fk.views import prodifk
from fkip.views import prodifkip
from ft.views import prodift
from pascasarjana.views import prodipascasarjana
from profil.views import prodiprofil
from DOSEN.views import prodiDOSEN, tambah_DOSEN
from TENDIK.views import prodiTENDIK
from Mahasiswa.views import prodiMahasiswa

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tirtayasa/', proditirtayasa),
    path('faperta/', prodifaperta),
    path('feb/', prodifeb),
    path('fh/', prodifh),
    path('fisip/', prodifisip),
    path('fk/', prodifk),
    path('fkip/', prodifkip),
    path('ft/', prodift),
    path('pascasarjana/', prodipascasarjana),
    path('profil/', prodiprofil),
    path('DOSEN/', prodiDOSEN),
    path('tambah-DOSEN/', tambah_DOSEN),
    path('TENDIK/', prodiTENDIK),
    path('Mahasiswa/', prodiMahasiswa),
      
]
