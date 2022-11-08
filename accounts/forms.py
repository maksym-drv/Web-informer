from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django import forms
 
class SignUpForm(UserCreationForm):
    image = forms.ImageField(required=False)

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'image')
        
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['password1', 'password2']:
            self.fields[fieldname].help_text = None