from django.urls import path
from writerpanel.views import *
from django.conf import settings
from django.conf.urls.static import static   
    
#writers
urlpatterns = [
path('',ListPosts.as_view(),name='my_writings'),
path('Haber_düzenle/<slug:slug>/',DetailPosts.as_view(),name='edit_news'),
path('Makale_düzenle/<slug:slug>/',DetailArticle.as_view(),name='edit_article'),
path('Haber_ekle/',AddPosts.as_view(),name='add_news'),
path('Makale_ekle/',AddArticle.as_view(),name='add_article'),
path('Haber_düzenle/<slug:slug>/delete/', DeletePostsView.as_view(),name='delete'),
path('Makale_düzenle/<slug:slug>/delete/', DeleteArticleView.as_view(),name='deletearticle'),
]
urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)