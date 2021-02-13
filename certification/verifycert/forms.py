from django import forms

class CertificateForm(forms.Form):
    Certificate_Number = forms.CharField(max_length=30)