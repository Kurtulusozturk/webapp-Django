from django.shortcuts import render


def yazi(request):
    context = {
        'isim':'Kurtuluş'
    }
    return render(request,'website/iletisim.html',context=context)