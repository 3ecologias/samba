# -*- coding: utf-8 -*-
from django import forms
from django.core.mail import send_mail, BadHeaderError
from django.core.mail import EmailMessage
from django.template.loader import get_template
from django.template import Context

class ContactUs(forms.Form):

    name = forms.CharField(required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Nome *', 'id': 'name', 'class': 'form-control mb-2', 'type': 'text'}))

    email = forms.EmailField(required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Email *', 'id': 'email', 'class': 'form-control mb-2'}))

    message = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'placeholder': 'Mensagem *', 'id': 'message', 'class': 'form-control mb-2', 'rows': '4'})
    )

    def send_email(self):
        name = self.cleaned_data['name']
        from_email = self.cleaned_data['email']
        message = self.cleaned_data['message']
        subject = 'SAMBA - Contato'

        try:
            email = EmailMessage(subject+" de "+name, message, from_email,['admin@3ecologias.net'])
            email.content_subtype = "html"
            email.send()
        except BadHeaderError:
            raise ValidationError("Cabeçalho inválido")

class SignUp(forms.Form):

    name = forms.CharField(required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Nome *', 'id': 'name', 'class': 'form-control mb-2', 'type': 'text'}))

    email = forms.EmailField(required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Email *', 'id': 'email', 'class': 'form-control mb-2'}))

    message = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Telefone *', 'id': 'message', 'class': 'form-control mb-2', 'type': 'tel' })
    )

    def send_email(self):
        name = self.cleaned_data['name']
        from_email = self.cleaned_data['email']
        message = self.cleaned_data['message']
        subject = 'SAMBA - Orçamento'

        try:
            email = EmailMessage(subject+" de "+name, message, from_email,['admin@3ecologias.net'])
            email.content_subtype = "html"
            email.send()
        except BadHeaderError:
            raise ValidationError("Cabeçalho inválido")
