from django import forms
from django.forms import ModelForm
from creditoapp.models import Werknemer


class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )


class WerknemersForm(ModelForm):
    class Meta:
        model = Werknemer
        fields = ['organisatie', 'voornaam',
                'tussenvoegsel', 'achternaam',
                  'email', 'rol',
                  ]


class UpdateForm(ModelForm):
    class Meta:
        model = Werknemer
        fields = ['organisatie', 'voornaam',
                  'tussenvoegsel', 'achternaam',
                  'email', 'rol', 'wachtwoord',
                  ]
        wachtwoord = forms.CharField(widget=forms.PasswordInput)
        widgets = {'wachtwoord': forms.PasswordInput(), }


class WerknemerSearchForm(forms.Form):
    search_text = forms.CharField(
        required=False,
        label='Search!',
        widget=forms.TextInput(attrs={'placeholder': 'search here!'})
    )

