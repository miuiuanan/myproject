from django import forms


class TemplateForm(forms.Form):
    name = forms.CharField(label="Name")
    subtitle = forms.CharField(required=False)
    image = forms.FileField()
    price = forms.CharField(required=False)
    hitcount = forms.CharField(required=False)
