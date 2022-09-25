from django.views.generic import ListView
from website.models.makale import MakalelerModel
from .forms import  UpdatePostsForm, UpdateArticlesForm
from website.models.yazi import YazilarModel
from django.views.generic.edit import UpdateView,CreateView,DeleteView
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.contrib import messages


User=get_user_model()


class AddPosts(PermissionRequiredMixin,LoginRequiredMixin,CreateView): #DÜZENLEMESİ GEREKEN FİELDS KISIMLARI VAR
    model = YazilarModel
    template_name = "writers/add-news.html"
    success_url = '/yazarpanel/'
    fields = ['resim','baslik','icerik',]
    permission_required = 'website.add_yazilarmodel'
        
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.yazar = self.request.user
        self.object.save()
        return super(AddPosts,self).form_valid(form)

    def handle_no_permission(self):
        # add custom message
        messages.error(self.request, 'You have no permission')
        return super(AddPosts, self).handle_no_permission()


class  ListPosts(PermissionRequiredMixin,LoginRequiredMixin,ListView):
    model = YazilarModel
    template_name = "writers/my-writings.html"
    permission_required = 'website.view_yazilarmodel'

    def get_context_data(self ,**kwargs):
        context = super(ListPosts, self).get_context_data(**kwargs)
        context['writers']=YazilarModel.objects.filter(yazar=self.request.user).order_by('-olusturulma_tarihi')
        context['articles'] = MakalelerModel.objects.all().filter(yazar=self.request.user).order_by('-olusturulma_tarihi')
        return context

    # def get_queryset(self):
    #     if self.kwargs.get('pk'):
    #         text_writer = YazilarModel.objects.filter(
    #             yazar=self.kwargs.get('pk')).values('yazar_id')

    #         return User.objects.filter(id__in=text_writer, roles=Role.WRITER)

    #     return User.objects.all()
    
    
#yazı haber 
class  DetailPosts(PermissionRequiredMixin,LoginRequiredMixin,UpdateView):
    model = YazilarModel
    template_name = "writers/edit-news.html"
    context_object_name = 'post'
    success_url = '/yazarpanel/'
    form_class = UpdatePostsForm
    permission_required = 'website.view_yazilarmodel'


class DeletePostsView(PermissionRequiredMixin,LoginRequiredMixin,DeleteView):
    model = YazilarModel
    success_url = '/yazarpanel/'   
    template_name = "writers/delete.html"
    permission_required = 'website.delete_yazilarmodel'


#makale

class AddArticle(PermissionRequiredMixin,LoginRequiredMixin,CreateView):#DÜZENLEMESİ GEREKEN FİELDS KISIMLARI VAR
    model = MakalelerModel
    template_name = "writers/add-article.html"
    success_url = '/yazarpanel/'
    fields =  ['baslik','makale',]
    permission_required = 'website.add_makalelermodel'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.yazar = self.request.user
        self.object.save()
        return super(AddArticle,self).form_valid(form)


class  DetailArticle(PermissionRequiredMixin,LoginRequiredMixin,UpdateView):
    model = MakalelerModel
    template_name = "writers/edit-article.html"
    context_object_name = 'article'
    success_url = '/yazarpanel/'
    form_class = UpdateArticlesForm
    permission_required = 'website.view_makalelermodel'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.makale=form.cleaned_data['makale']
        # self.object.makale = form.request.FILES['makale']
        self.object.save()
        return super(DetailArticle,self).form_valid(form)


class DeleteArticleView(PermissionRequiredMixin,LoginRequiredMixin,DeleteView):
    model = MakalelerModel
    success_url = '/yazarpanel/'   
    template_name = "writers/delete.html"  
    permission_required = 'website.delete_makalelermodel'
    
