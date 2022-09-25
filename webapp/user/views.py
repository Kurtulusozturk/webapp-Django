from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.views import redirect_to_login
from django.shortcuts import redirect, render
from user.forms import CustomUserCreationForm
from django.views.generic.edit import UpdateView
from django.views.generic import DetailView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import Group
User = get_user_model()


def register(request):
    if request.method == "POST":
        form= CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            user_group = Group.objects.get(name='User') 
            user.groups.add(user_group)
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            first_name = form.cleaned_data['first_name']
            user = authenticate(email=email,password=password,first_name=first_name)
            login(request,user )
            # messages.success(request,("Kayıt başarılı"))
            return redirect('home')
    else:
        form= CustomUserCreationForm()
    return render(request,'users/register.html',{
        'form':form,
    })

    
@login_required
def home(request):
    context = {"title": "SEISMOCODE"}
    return render(request, 'main/mainpage.html', context=context)


def signin(request):
    if request.method == "POST":

        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, "Kullanıcı kayıtlı değil")
            return redirect('login')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Kullanıcı aktif değil!")
                return redirect('login')
        else:

            messages.error(request, "Kullanıcı adı veya şifre hatalı!")
            return redirect('login')

    context = {"title": "signin"}
    # print("post", request.POST)
    return render(request, 'users/login.html', context=context)

@login_required
def signout(request):
    logout(request)
    return redirect('login')

def editprofile(request):
    return render(request,'users/edit-profile.html')
    


class  Usereditprofile(UpdateView):
    model = User
    fields = ['first_name','last_name','email']
    template_name = "users/edit-profile-info.html"
    # context_object_name = 'user'
    success_url = '/kullanıcı/profil/'


    def get_object(self):
        return User.objects.get(pk=self.request.user.id)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('editprofile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'users/change-password.html', {
        'form': form
    })


#Permissions
# class WriterPermissions(PermissionRequiredMixin):
#     raise_exception = False

#     def has_permission(self):

#         if self.request.user.is_superuser:
#             return True
#         return self.request.user.is_staff

#     def handle_no_permission(self):
#         messages.error(self.request, "Yetkiniz yok ")
#         return redirect(('home'))


# class EditNewsView(PermissionRequiredMixin,UpdateView):
#     raise_exception = True #403 hatası yazdırır
#     permission_required = ('yazi.change_yazi')
#     permission_denied_message = "" #hata mesajı yazdırır
#     login_url ='login' # başarısız olursa nereye yönlendiricek
#     redirect_field_name = 'next'

#     model = YazilarModel
#     # form_class = AddForm
#     template_name = 'writers/edit-news.html'
#     success_url = '/Yayimlarim/Haber_düzenle/' #başarılı olursa yöneldirileceği sayfa
    
# class AddNewsView(WriterPermissions,CreateView):
#     raise_exception = True #403 hatası yazdırır
#     permission_required = ('yazi.add_yazi')
#     permission_denied_message = "" #hata mesajı yazdırır
#     login_url ='login' # başarısız olursa nereye yönlendiricek
#     redirect_field_name = 'next'

#     model = YazilarModel
#     # form_class = AddForm
#     template_name = 'writers/add-news.html'
#     success_url = '/Yayimlarim/Haber_ekle/'



    # if request.method == 'POST':
    #     form = CustomUserCreationForm(request.POST)
    #     if form.is_valid():
            
    #         email = form.cleaned_data()
    #         raw_password = form.cleaned_data.get('password1')
            
    #         user = authenticate(email=email, password=raw_password)
    #         user = form.save()
    #         login(request, user)
    #         return redirect('home')
        
    # else:
    #     form = CustomUserCreationForm()
    
    # return render(request, 'users/register.html', {'form': form})    
