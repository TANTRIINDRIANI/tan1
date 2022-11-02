from django.forms import ModelForm
from DOSEN.models import DOSEN

class FormDOSEN(ModelForm):
    class Meta:
        model = DOSEN
        fields = '__all__'

