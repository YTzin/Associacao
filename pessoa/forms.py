from django import forms
from .models import Pessoas, Conjuge, Dependentes
import re

class CadastroPessoa(forms.ModelForm):
    data_nascimento = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
       
    )
    data_cadastramento = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        
    )
    data_expedicao = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
    
    )
    data_emissao = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        
    )
    telefone = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={'placeholder': '(00) 00000-0000'}),
        label='Telefone'
    )
    cpf = forms.CharField(
        max_length=14,
        widget=forms.TextInput(attrs={'placeholder': '000.000.000-00'}),
        label='CPF'
    )
    
    def clean_telefone(self):
        telefone = self.cleaned_data.get('telefone')
        # Adicione a lógica de validação para telefone
        if not re.match(r'^\(\d{2}\) \d{5}-\d{4}$', telefone):
            raise forms.ValidationError('Telefone inválido. Use o formato (00) 00000-0000.')
        return telefone

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        # Adicione a lógica de validação para CPF
        if not re.match(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', cpf):
            raise forms.ValidationError('CPF inválido. Use o formato 000.000.000-00.')
        return cpf
    class Meta:
        model = Pessoas
        fields = '__all__'


class FormConjuge(forms.ModelForm):
    class Meta:
        model = Conjuge
        fields = '__all__'

class FormDependente(forms.ModelForm):
    class Meta:
        model = Dependentes
        fields = '__all__'