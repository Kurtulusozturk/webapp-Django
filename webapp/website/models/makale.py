from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse
from website.abstract_model import DateAbstractModel
from user.models import User


class MakalelerModel(DateAbstractModel):
    baslik = models.CharField(max_length=50)
    makale = models.FileField(upload_to='makale_pdf/',null=True)
    slug = AutoSlugField(populate_from = 'baslik', unique = True)#kaldır
    #çoktan çoğa db ilişkisi
    #models.CASCADE kullanıcı silinir ise yazılarını da siler
    #related name ler ise ilişkilendirme isimleri
    yazar = models.ForeignKey(User,on_delete=models.SET_NULL,related_name='makaleler',null=True) 

    class Meta:
        verbose_name = 'makale'
        verbose_name_plural = 'makaleler'

    def get_absolute_url(self):
            return reverse('article-details', kwargs={'slug': self.slug})

    def __str__(self) :
        return  self.baslik