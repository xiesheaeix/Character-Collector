from django.forms import ModelForm
from .models import Token

class TokenForm(ModelForm):
    class Meta:
        model = Token
        fields = ['date']
