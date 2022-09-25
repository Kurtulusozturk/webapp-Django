from django.shortcuts import render


def iletisim(request):
    context = {
        'isim':'Kurtuluş'
    }
    return render(request,'website/iletisim.html',context=context)
