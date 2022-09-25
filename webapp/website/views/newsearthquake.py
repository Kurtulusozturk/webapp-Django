from django.views.generic import ListView,DetailView
from website.models.yazi import YazilarModel
from django.core.paginator import Paginator


class  NewsViewListView(ListView):
    model = YazilarModel
    template_name = "website/newsearthquake.html"
    queryset = YazilarModel.objects.all().order_by('-olusturulma_tarihi')
    paginate_by = 3
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['posts'] = YazilarModel.objects.all().order_by('-olusturulma_tarihi')[:8]
    #     #paginator
    #     # news_paginator =Paginator(context,2)
    #     # page= news_paginator.get_page(1) 
    #     return context
class  NewsDetailView(DetailView):
    model = YazilarModel
    template_name = "website/news-details.html"
    context_object_name = 'post' 