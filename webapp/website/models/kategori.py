from django.db import models
from autoslug import AutoSlugField


#db oluşurtuyoruz
class KategoriModel(models.Model):
    isim=models.CharField(max_length=30,blank=False,null=False)
    kategori_url=models.CharField(max_length=30,blank=False,null=False,default='#')
    slug= AutoSlugField(populate_from='isim',unique=True)

    class Meta:
        verbose_name='kategori'
        verbose_name_plural='kategoriler'

    #adminde db objectlerin nasıl gözükeceğini ayarlar
    def __str__(self): 
        return self.isim
