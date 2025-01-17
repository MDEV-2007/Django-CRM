from django import forms
from .models import Leads
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


User = get_user_model()

class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Leads
        fields = ('first_name', 'last_name', 'age', 'phone_number', 'agent')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'input-field' 
            })

         
class LeadForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField(min_value=0)




class UsernameField(forms.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['widget'] = forms.TextInput(attrs={'class': 'custom-username-field', 'placeholder': 'Enter your username'})
        super().__init__(*args, **kwargs)

class CustomUserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email')

    username = UsernameField()