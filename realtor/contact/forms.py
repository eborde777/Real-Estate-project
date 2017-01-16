from django import forms


class ContactForm(forms.Form):
    firstname = forms.CharField(widget=forms.TextInput)
    lastname = forms.CharField(widget=forms.TextInput)
    email = forms.EmailField()
    phone = forms.CharField(widget=forms.TextInput, required=False)
    description = forms.CharField(widget=forms.Textarea)

