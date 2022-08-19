from django import forms
from .models import Model1


class InputForms(forms.Form):
    textarea = forms.CharField(
        max_length=5000,
        required=False,
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Type here...",
            }
        )
    )


class TestForm(forms.ModelForm):
    class Meta:
        model = Model1
        fields = (
            "fullname", "age", "email", "password", "graduated", "reason", "level"
        )
        widgets = {
            "fullname": forms.TextInput(attrs={"class": "form-control"}),
            "age": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "password": forms.PasswordInput(attrs={"class": "form-control"}),
            "graduated": forms.BooleanField(),
            "reason": forms.Textarea(attrs={"class": "form-control"}),
            "level": forms.Select(attrs={"class": "form-control"}),
        }
