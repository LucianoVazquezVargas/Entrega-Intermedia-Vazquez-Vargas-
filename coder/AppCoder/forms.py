from django import forms 

class PersonaForm(forms.Form):
    nombre= forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)

class HeladoForm(forms.Form):
    nombre=forms.CharField(max_length=50)

class NotasForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)   
    email=forms.EmailField()
    