from django.shortcuts import render

# Create your views here.
def prodiMahasiswa(request):
    return render(request, 'indexMahasiswa.html')
