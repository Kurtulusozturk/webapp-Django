import os
from django.http import HttpResponse, HttpResponseNotFound
from django.views.generic import ListView,DetailView
from django.core.files.storage import FileSystemStorage
from website.models.makale import MakalelerModel


class  ArticlesViewListView(ListView):
    model = MakalelerModel
    template_name = "website/articles.html"
    queryset = MakalelerModel.objects.all().order_by('-olusturulma_tarihi')
    paginate_by = 20
 
# def show_pdf(request):
#     filepath = os.path.join('media/makale_pdf', 'deprem.pdf')
#     return FileResponse(open(filepath, 'rb'), content_type='application/pdf')    

