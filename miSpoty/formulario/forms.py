from django import forms

class SingUpForm(forms.Form):
    primer_nombre=forms.CharField(max_length=200)
    apellido=forms.CharField(max_length=200)
    email=forms.EmailField(max_length=200)
    password=forms.CharField(widget=forms.PasswordInput())
    def clean_email(self):
        """Validate that the email doesn't exist in the database."""
        data = self.cleaned_data["email"]
        if User.objects.filter(email=data).count() > 0:
            raise forms.ValidationError("This email already exists.")   
        return data
