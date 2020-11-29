from django import forms
from .models import Denuncia

class DenunciaForm(forms.ModelForm): 
    class Meta:
        model = Denuncia
        fiels = ["Nome_da_rua", "Bairro", "Ponto_de_referencia", "Cidade", "Estado", "Cep", "Problematica", "Titulo", "Campo_De_Texto", "Anexar_Imagens"]