from django import forms

class EntradaFormulario(forms.Form):
    titulo = forms.CharField()
    subtitulo = forms.CharField()
    cuerpo = forms.CharField(widget=forms.Textarea)
