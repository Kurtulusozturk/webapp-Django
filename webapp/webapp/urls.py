"""webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static  #media dosyası yapmak için 
from django.conf import settings            #media dosyası yapmak için 
from django.contrib import admin
from django.urls import path,include

admin.site.site_title = 'Seismo'
admin.site.site_header = 'Seismo Administrator'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    # path('app/', include('app.urls')),
    path('kullanıcı/',include('user.urls')), 
    path('adminpanel/',include('adminpanel.urls')),
    path('yazarpanel/',include('writerpanel.urls')),
    # path('writer/',include('writerpanel.urls')),
]
urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) #media dosyası yapmak için settings de de ayarlar varfrom django.urls import include, path
urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
