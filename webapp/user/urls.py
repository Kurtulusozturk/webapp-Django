from django.urls import path
from user.views import Usereditprofile, register, signin,signout,home,editprofile
# from django.conf.urls import url
from user import views


urlpatterns = [
    path('',home,name='register'),
    path('login/', signin,name='login'),
    path('Kaydol', register,name='register'),
    path('logout/',signout,name='logout'),
    path('profil/',editprofile,name='editprofile'),
    path('profil/duzenle/',views.Usereditprofile.as_view(),name='editprofileuser'),
    path(r'^password/$', views.change_password, name='change_password'),
]
