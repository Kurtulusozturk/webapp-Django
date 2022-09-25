from cProfile import label
from operator import mod
from pyexpat import model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from user.models import User
from django import forms


User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label = "Email")
    first_name = forms.CharField(label = "first name")
    last_name = forms.CharField(label = "last name")
    password1 = forms.CharField(widget=forms.PasswordInput)
    # roles = forms.CharField(label="Roles")
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email','password1','password2','first_name','last_name')


    # def clean_email(self):
    #     email=self.cleaned_data['email']
    #     if User.objects.filter(email=self.cleaned_data['email']).exists():
    #         raise forms.ValidationError("Girdiğiniz email ile kayıt yapılmış")    
    #     return email















# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

 
# class SignUpForm(UserCreationForm):
#     first_name = forms.CharField(max_length=30, required=True, help_text='Optional.')
#     last_name = forms.CharField(max_length=30, required=True, help_text='Optional.')
#     email = forms.EmailField(max_length=254, required=True,help_text='Required. Inform a valid email address.')
#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
#     def clean_email(self):
#         email=self.cleaned_data['email']
#         if User.objects.filter(email=self.cleaned_data['email']).exists():
#             raise forms.ValidationError("Girdiğiniz email ile kayıt yapılmış")    
#         return email
#     def clean_username(self):
#         username=self.cleaned_data['username']
#         if User.objects.filter(username=self.cleaned_data['username']).exists():
#             raise forms.ValidationError("Girdiğiniz username ile kayıt yapılmış")
#         return username  
   
# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User


# # Create your forms here.

# class NewUserForm(UserCreationForm):
# 	email = forms.EmailField(required=True)

# 	class Meta:
# 		model = User
# 		fields = ("username", "email", "password1", "password2")

# 	def save(self, commit=True):
# 		user = super(NewUserForm, self).save(commit=False)
# 		user.email = self.cleaned_data['email']
# 		if commit:
# 			user.save()
# 		return user













# from django import forms
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm  
# from django.contrib.auth import get_user_model

# User=get_user_model()

# class Singup(UserCreationForm):
#     username = forms.CharField(max_length=6, required=False, help_text='Optional.')
#     first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
#     last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
#     email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
  

#     USERNAME_FIELD='email'
#     class Meta:
#         model = User
#         fields = ('username','first_name', 'last_name', 'email', 'password1', 'password2', )
    
    
#     def clean(self):
#         username=self.cleaned_data.get("username")
#         first_name=self.cleaned_data.get("first_name")
#         last_name=self.cleaned_data.get("last_name")
#         email=self.cleaned_data.get("email")
#         password=self.cleaned_data.get("password")
#         repassword=self.cleaned_data.get("repassword")


#         if password and repassword and password != repassword:
#             raise forms.ValidationError('Şifreler uyuşmamaktadır.')
    

#         values = {
#             'username':username,
#             'email':email,
#             'first_name':first_name,
#             'last_name':last_name,
#             'password':password
#         }

#         return values
