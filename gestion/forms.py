from django import forms
from gestion.models import Usuario, LugarPrestamo
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(min_length=8, widget=forms.PasswordInput)
    username = forms.CharField(max_length=150)
    class Meta:
        model = User
        fields = ('username',)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])

        if commit:
            user.save()
        return user

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        exclude = ['user', 'penalizado']

class LugaresPrestamoForm(forms.ModelForm):
    class Meta:
        model = LugarPrestamo
        fields = ['nombre']