from django import forms

class EntradaFormulario(forms.Form):
    titulo = forms.CharField()
    autor = forms.CharField()
    cuerpo = forms.CharField(widget=forms.Textarea)
