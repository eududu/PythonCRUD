from django.forms import ModelForm
from app.models import Pessoas

class PessoasForm(ModelForm):
    class Meta:
        model = Pessoas
        fields = ['nome', 'idade']


