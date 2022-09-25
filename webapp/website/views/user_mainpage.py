from django.shortcuts import render


def kullanici_arayuzu(request):
    return render(request,'main/user_mainpage.html')#,context={}