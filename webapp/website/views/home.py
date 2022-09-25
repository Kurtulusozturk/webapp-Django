from django.shortcuts import render
from website.models.kategori import KategoriModel
from website.models.yazi import YazilarModel



def index(request):
    kategoriler = KategoriModel.objects.all()
    yazilar = YazilarModel.objects.all().order_by('-olusturulma_tarihi')[:3]
    context = {
        'kategoriler': kategoriler,
        'yazilar': yazilar
    }
    return render(request,'main/mainpage.html',context = context)
