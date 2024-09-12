from django import forms
from django.contrib.auth.views import LoginView
from QRBox.models import Customer


class SignUpForm(forms.ModelForm):
    email = forms.EmailField(required=True, label="Email")
    name = forms.CharField(required=True, label="Name")
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = Customer
        fields = ('email', 'name', 'password1', 'password2')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
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
    size = forms.IntegerField(label='QR code Size (1-40)', min_value=1, max_value=40)
    transparent = forms.BooleanField(label='Transparent background', required=False)
    background = forms.ImageField(label='Custom background', required=False)
    logo = forms.ImageField(label='Logo', required=False)
    color = forms.CharField(label='Color', widget=forms.TextInput(attrs={'type': 'color', 'value': '#ff0000'}))