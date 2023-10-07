from django import forms 
from django.contrib.auth.models import User 
from .models import UserProfile
from django.contrib.auth.forms import SetPasswordForm 
from bookstore.models import BookInfo 


DEPARTMENTS = (
    ("",""),
    ("computer science","computer science"),
    ("marketing","marketing"),
    ("accounting and finance","accounting and finance"),

)

class SignUpForm(forms.ModelForm):
    password = forms.CharField(label="Password",widget=forms.PasswordInput) 
    confirm_pwd = forms.CharField(label="Confirm Password",widget=forms.PasswordInput)   
   
    class Meta:
        model = User 
        fields = ["username","first_name","last_name","email"]

    def clean_confirm_pwd(self):

        cd = self.cleaned_data

        if cd["password"] != cd["confirm_pwd"]:
            raise forms.ValidationError("Password don't match")

        return cd["confirm_pwd"]


class ProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile 
        fields = ["bio","department"]
       
class ProfileEditForm(forms.ModelForm):

    class Meta:
        model = UserProfile 
        fields = ["profile_photo","bio","department"]
       
class UserEditForm(forms.ModelForm):

    class Meta:
        model = User 
        fields = ["username","first_name","last_name","email"]

        widgets = {
             'username': forms.TextInput(attrs={'placeholder':"Enter you username"}),
             'first_name': forms.TextInput(attrs={'placeholder':"Enter your first name"}),
             'last_name': forms.TextInput(attrs={'placeholder':"Enter your last name"})
        }

class LoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)

    
class SetPassWordForm(SetPasswordForm):

        class Meta:
            model = User 
            fields = ["new_password1","new_password2"] 

class UploadFileForm(forms.ModelForm):
    
    class Meta:
        model = BookInfo 
        fields = ["book_file"]

class EditBookForm(forms.ModelForm):

        class Meta:
            model = BookInfo
            fields = ["title","author","pages","published_year","size","description","language","category","department"]

            widgets = {
              'description': forms.Textarea(attrs={"rows":2,"placeholder":"Enter description about book. like summary"}),
              'department': forms.TextInput(attrs={'placeholder':"for which department this book applicable?"})
            }
