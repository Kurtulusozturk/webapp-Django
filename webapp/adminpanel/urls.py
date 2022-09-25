from django.urls import path
from . import views
# from website.views import *
from adminpanel.views import ListWriters,DetailWriters,Adminpanel,ListReaders,DetailReaders,createWriter,ReaderEditView,WriterEditView,ReaderDeleteView,WriterDeleteView


urlpatterns = [
    path('', Adminpanel,name='Adminpanel'),
    path('listwriters/',ListWriters.as_view(),name='listwriters'),
    path('detail-writers/<int:pk>/', DetailWriters.as_view(), name='detail-writers'),
    path('listreaders/',ListReaders.as_view(),name='listreaders'),
    path('detail-readers/<int:pk>/', DetailReaders.as_view(), name='detail-readers'),
    path('yazar-olustur/', views.createWriter, name='create-writer'),
    path('detail-writers/<int:pk>/edit', WriterEditView.as_view(), name='edit-writers'),
    path('detail-readers/<int:pk>/edit', ReaderEditView.as_view(), name='edit-readers'),
    path('detail-readers/<int:pk>/edit/delete', ReaderDeleteView.as_view(), name='delete-reader'),
    path('detail-readers/<int:pk>/edit/delete', WriterDeleteView.as_view(), name='delete-writer'),
]
