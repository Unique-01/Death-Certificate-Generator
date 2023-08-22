from django import forms
# from .models import Certificate
class DateInput(forms.DateInput):
    input_type = 'date'


class CertificateForm(forms.Form):
    full_name = forms.CharField(max_length=500)
    death_date = forms.DateField(widget=DateInput())
    death_location = forms.CharField(max_length=1000)
    date_of_birth = forms.DateField(widget=DateInput())
    evidence_of_death = forms.FileField(help_text="E.g. Doctor's Clearance")