from django.shortcuts import render,redirect
from user.models import User
from django.views.generic import ListView,DetailView
from django.contrib.auth import get_user_model
from user.forms import *
from adminpanel.forms import *
from django.views.generic.edit import UpdateView,DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import Group


User = get_user_model()

@permission_required('user.view_user', raise_exception=True)
def Adminpanel(request):
     return render(request,'adminpanel/adminpanel.html')

#WRİTER

class  ListWriters(PermissionRequiredMixin,ListView):
    model = User
    template_name = "adminpanel/listwriters.html"
    permission_required = 'user.view_user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['listwriters'] = User.objects.all().order_by('first_name').filter(roles='2')
        return context

class  DetailWriters(PermissionRequiredMixin,DetailView):
    model = User
    template_name = "adminpanel/detailusers.html"
    context_object_name = 'writer' 
    permission_required = 'user.view_user'

class WriterEditView(PermissionRequiredMixin,UpdateView):
    model=User
    form_class = UpdateUserForm
    template_name = "adminpanel/detailusersedit.html"
    context_object_name = 'writer'
    permission_required = 'user.change_user'

class WriterDeleteView(PermissionRequiredMixin,DeleteView):
    model=User
    # form_class = UpdateUserForm
    template_name = "adminpanel/detailusersedit.html"
    success_url = '/adminpanel/listwriters/'
    context_object_name = 'writer' 
    permission_required = 'user.delete_user'

#READER

class  ListReaders(PermissionRequiredMixin,ListView):
    model = User
    template_name = "adminpanel/listreaders.html"
    queryset = User.objects.all().order_by('first_name').filter(roles='1')
    paginate_by = 25
    permission_required = 'user.view_user'
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['listreaders'] = User.objects.all().filter(roles='1')
    #     return context

class  DetailReaders(PermissionRequiredMixin,DetailView):
    model = User
    template_name = "adminpanel/detailusers.html"
    context_object_name = 'writer' 
    permission_required = 'user.view_user'

class ReaderEditView(PermissionRequiredMixin,UpdateView):
    model=User
    form_class = UpdateUserForm
    template_name = "adminpanel/detailusersedit.html"
    success_url = '/adminpanel/listreaders/'
    context_object_name = 'writer' 
    permission_required = 'user.change_user'

class ReaderDeleteView(PermissionRequiredMixin,DeleteView):
    model=User
    # form_class = UpdateUserForm
    template_name = "adminpanel/detailusersedit.html"
    success_url = '/adminpanel/listreaders/'
    context_object_name = 'writer' 
    permission_required = 'user.delete_user'

@permission_required('user.view_user', raise_exception=True)
def createWriter(request): #admin panelinde kullanıcı oluşturma yeri
    form=AdminAddUserForm()
    if request.method == 'POST':
        # print('Post çıktısı:',request.POST)
        form=AdminAddUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            if request.POST['roles']=='2':
                user_group = Group.objects.get(name='Writer') 
                user.groups.add(user_group)
                return redirect('/adminpanel/listwriters/')
            elif request.POST['roles']=='1':
                user_group = Group.objects.get(name='User') 
                user.groups.add(user_group)
                return redirect('/adminpanel/listreaders/')
    context={'form':form}
    return render (request,'adminpanel/createwriter.html')

# def updateUser(request,pk):

#     user=User.objects.get(id=pk)
#     form=UpdateUserForm(instance=user)
#     if request.method == 'POST':
#         print('Post çıktısı:',request.POST)
#         form=UpdateUserForm(request.POST,instance=user)
#         if form.is_valid():
#             form.save()
#             if request.POST['roles']=='2':
#                 return redirect('/adminpanel/listwriters/')
#             elif request.POST['roles']=='1':
#                 return redirect('/adminpanel/listreaders/')
#     context={'form':form}
#     return render (request,'adminpanel/detailusers.html')
