from django import forms


class Formulario(forms.Form):
	nombre = forms.CharField(label='Ingrese Nombre',widget=forms.TextInput(
		attrs={
			'class':'form-control',
            'placeholder':'Nombre'
		}))

	apellido = forms.CharField(label='Ingrese Apellido',widget=forms.TextInput(
		attrs={
			'class':'form-control',
            'placeholder':'Apellido'
		}))

	edad = forms.IntegerField(label='Ingrese Edad',widget=forms.TextInput(
		attrs={
			'class':'form-control',
			'type':'number',
            'placeholder': 'Edad'
		}))

	password = forms.CharField(label='Ingrese Password',widget=forms.TextInput(
		attrs={
			'class':'form-control',
			'type':'password',
            'placeholder':'Contraseña'
		}))	
	email = forms.CharField(label='Ingrese Email',widget=forms.TextInput(
		attrs={
			'class':'form-control',
			'type':'mail',
            'placeholder':'Mail'
		}))

class Formulario_desafio(forms.Form):
        nombre_usuario = forms.CharField(label='Ingrese Nombre de Usuario',widget=forms.TextInput(
		attrs={
			'class':'form-control',
            'placeholder':'Nombre_usuario'
		}))
        
        numero_favorito = forms.IntegerField(label='Ingrese su Numero Favorito',widget=forms.TextInput(
		attrs={
			'class':'form-control',
			'type':'number',
            'placeholder': 'Numero_favorito'
		}))
        
	correo = forms.CharField(label='Ingrese su Correo',widget=forms.TextInput(
		attrs={
			'class':'form-control',
			'type':'mail',
            'placeholder':'Correo'
		}))
	
	contraseña = forms.CharField(label='Ingrese su Contraseña',widget=forms.TextInput(
		attrs={
			'class':'form-control',
			'type':'password',
            'placeholder':'Contraseña'
		}))

	confirmar_contraseña = forms.CharField(label='Confirme su Contraseña',widget=forms.TextInput(
		attrs={
			'class':'form-control',
			'type':'password',
            'placeholder':'Confirmar_contraseña'
		}))

        animal_favorito = forms.CharField(label='Ingrese su Animal Favorito',widget=forms.TextInput(
		attrs={
			'class':'form-control',
            'placeholder':'Animal_favorito'
		}))
