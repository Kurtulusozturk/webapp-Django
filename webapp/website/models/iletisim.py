from django.db import models


class IletisimModel(models.Model):
    email = models.EmailField(max_length=250)
    isim= models.CharField(max_length=80)
    soyisim = models.CharField(max_length=80)
    mesaj = models.TextField()
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True) # auto_now_add her ekleme yapıldıgında tarihi güncelle 

    class Meta:
        verbose_name = 'Iletisim'
        verbose_name_plural = 'Iletisimler'

    def __str__(self):
        return self.email
