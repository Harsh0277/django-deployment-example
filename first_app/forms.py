from django import forms
from django.core import validators
from first_app.models import AccessRecord,UserProfileInfo
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model=UserProfileInfo
        fields=('portfolio_site','profile_pic')

class FormName(forms.ModelForm):
    class Meta:
        model=AccessRecord
        fields='__all__'

# def check_for_h(value):
#     if value[0].lower()!='h':
#         raise forms.ValidationError("Start name with h")

# class FormName(forms.Form):
#     #name=forms.CharField(validators=[check_for_h])
#     name = forms.CharField()
#     email=forms.EmailField()
#     verify_email=forms.EmailField(label="Enter your email again: ")
#     text=forms.CharField(widget=forms.Textarea)
#     botcatcher=forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])
#
#     def clean(self):
#         all_clean_data=super().clean()
#         email=all_clean_data['email']
#         vmail=all_clean_data['verify_email']
#         if email!=vmail:
#             raise forms.ValidationError("Make sure that emails match")

    # def clean_botcatcher(self):
    #     botcatcher=self.cleaned_data['botcatcher']
    #     if len(botcatcher)>0:
    #         raise forms.ValidationError("Gotcha you Bot!!!")
    #     return botcatcher