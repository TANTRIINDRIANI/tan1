from django.shortcuts import render
from DOSEN.models import DOSEN
from DOSEN.forms import FormDOSEN


# Create your views here.
def prodiDOSEN(request):
    return render(request, 'indexDOSEN.html')

def tambah_DOSEN(request):
    form = FormDOSEN()

    konteks = {
        'form' : form,
    }

    return render(request, 'tambah-DOSEN.html', konteks)

