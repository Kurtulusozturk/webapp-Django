from django.urls import path
from website.views import *
from website.views.newsearthquake import NewsViewListView,NewsDetailView
from website.views.articles import  ArticlesViewListView
from django.conf import settings
from django.conf.urls.static import static   


urlpatterns = [
    path('', index,name='index'),
    path('Anasayfa/',index,name='home'),
    path('Anasayfa_kullanici/',kullanici_arayuzu,name='user_mainpage'),
    path('Iletisim/',iletisim,name='Iletisim'),   
    path('Deprem_Haberleri/',NewsViewListView.as_view(),name='newsearthquake'), 
    path('Deprem_Haberleri/detay/<slug:slug>/',NewsDetailView.as_view(),name='news-details'),
    path('Makaleler/',ArticlesViewListView.as_view(),name='articles'), 
    # path('Makaleler/pdf/',show_pdf,name='articles-pdf'), 
    # path('Deprem_Haberleri/detay/<slug:slug>/',ArticlesDetailView.as_view(),name='news-details'),

]
urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
