from django import forms
from apps.account.models import User
from .models import Address

__all__ = [
    'UserProfileForm',
    'UserCreateAddressForm'
]

class UserProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['phone_number'].disabled = True
        self.fields['email'].disabled = True

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = ('full_name','phone_number','email')

class UserCreateAddressForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Address
        exclude  = ('to',)