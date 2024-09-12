from django import forms
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, label=None)

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class CustomLoginView(LoginView):
    template_name = 'login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'QRBox: Login'
        return context


class QRCodeForm(forms.Form):
    data = forms.CharField(label='Enter URL', max_length=255, widget=forms.TextInput(attrs={
        'placeholder': 'Enter text or URL...',
        'class': 'form-control'})
    )
    size = forms.IntegerField(label='Size (1-40)', min_value=1, max_value=40)
    transparent = forms.BooleanField(label='Transparent background', required=False)
    custom_background = forms.ImageField(label='Custom background', required=False)
    logo = forms.ImageField(label='Logo', required=False)
    options = forms.ChoiceField(
        choices=[
            ('square', 'Square (default)'),
            ('circle', 'Circle'),
            ('triangle', 'Triangle'),
            ('star', 'Star'),
            ('diamond', 'Diamond'),
            ('waves', 'Waves'),
        ],
        label='Shape'
    )
    color = forms.CharField(label='Color', widget=forms.TextInput(attrs={'type': 'color', 'value': '#ff0000'}))
    animated = forms.BooleanField(label='Animated', required=False)