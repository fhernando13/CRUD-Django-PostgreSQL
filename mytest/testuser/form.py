from django.forms import ModelForm, EmailInput
from testuser.models import User

class Userform(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'email': EmailInput(attrs={'type':'email'})
        }
