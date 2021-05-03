from django import forms
from django.contrib.auth.models import User
from Hakunamatata.models import contactform, UserProfileInfo



class contactform_(forms.ModelForm):
    class Meta():
        model = contactform
        fields = '__all__' #it handel all the fields in your model



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')
#from user model we want these  field

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('dob','profile_pic')
#from UserProfileInfo model we want these  field




































#class ContactForm(forms.Form):
#    fullname = forms.CharField(widget=forms.TextInput(
#                    attrs={
#                        "class": "form-control",
#                        "placeholder": "Your full name"
#                    }
#
#
#
#                     ))
#     email    = forms.EmailField(widget=forms.EmailInput(
#                     attrs={
#                         "class": "form-control",
#                         "placeholder": "Your email"                    }))
#     content = forms.CharField(widget=forms.Textarea(
#                 attrs={
#                     'class': 'form-control',
#                     "placeholder": "Your message"
#                     }
#                 ))
