from django import forms
from .models import Objeto, Historico

class ObjForm(forms.ModelForm):
	objeto = forms.CharField(max_length=100, required=False)
	class Meta:
		model = Objeto
		fields = ('server', 'antena', 'code', 'objeto')

class HistForm(forms.ModelForm):
	objeto = forms.CharField(max_length=100, required=False)
	class Meta:
		model = Historico
		fields = ('server', 'antena', 'code', 'objeto')