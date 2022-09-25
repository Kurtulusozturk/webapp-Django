from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse
from ckeditor.fields import RichTextField
from website.abstract_model import DateAbstractModel
from user.models import User


class YazilarModel(DateAbstractModel):
    resim = models.ImageField(upload_to='yazi_resimler')
    baslik = models.CharField(max_length=50)
    icerik = RichTextField()
    slug = AutoSlugField(populate_from = 'baslik',unique = True)
    # kategoriler = models.ManyToManyField(KategoriModel, related_name='yazi') #çoktan çoğa db ilişkisi
    #models.CASCADE kullanıcı silinir ise yazılarını da siler
    #related name ler ise ilişkilendirme isimleri
    yazar= models.ForeignKey(User,on_delete=models.SET_NULL,related_name='yazilar',null=True) 

    def __str__(self):
         return self.yazar

    class Meta:
        verbose_name = 'yazi'
        verbose_name_plural = 'yazilar'

    def get_absolute_url(self):

            return reverse('news-details', kwargs={'slug': self.slug})

    def __str__(self) :
        return  self.baslik
