from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from user.models import User
from django import forms

# class WriterCreateForm(ModelForm):
#     class Meta:
#         model=User
#         fields=['first_name','last_name','email','roles']
class AdminAddUserForm(UserCreationForm):
    email = forms.EmailField(label = "Email")
    first_name = forms.CharField(label = "first name")
    last_name = forms.CharField(label = "last name")
    roles = forms.CharField(label = "roles")
    password1 = forms.CharField(widget=forms.PasswordInput)
    # roles = forms.CharField(label="Roles")
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email','password1','password2','first_name','last_name','roles')
class UpdateUserForm(ModelForm):
    email = forms.EmailField(label = "Email")
    first_name = forms.CharField(label = "first name")
    last_name = forms.CharField(label = "last name")
    is_active = forms.CharField(label='active')  
    class Meta:
        model=User
        fields=['first_name','last_name','email',"is_active","roles"]