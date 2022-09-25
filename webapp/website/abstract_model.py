from django.db import models
from django.utils import timezone


#birden fazla kod tekranını engellemek için db de gözükmeyen bir model tasarlanır yorum ve yazi da kullandık
class DateAbstractModel(models.Model):
    olusturulma_tarihi = models.DateTimeField(editable=False)# auto_now_add her ekleme yapıldıgında tarihi güncelle 
    duzenlenme_tarihi = models.DateTimeField()
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.olusturulma_tarihi = timezone.now()
        self.duzenlenme_tarihi = timezone.now()
        return super(DateAbstractModel, self).save(*args, **kwargs)