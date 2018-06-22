from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=20)
    subject = forms.CharField(max_length=100)
    message = forms.CharField(max_length=1000,widget=forms.Textarea)
    sender_address = forms.CharField(max_length=100)
    email = forms.EmailField()
