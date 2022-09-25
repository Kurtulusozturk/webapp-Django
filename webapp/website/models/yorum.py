from django.db import models
from website.models.yazi import YazilarModel
from website.abstract_model import DateAbstractModel


class YorumModel(DateAbstractModel):
    # yazan = models.ForeignKey('user', on_delete=models.CASCADE,related_name="yorum")
    yazi = models.ForeignKey(YazilarModel, on_delete=models.CASCADE,related_name="yorumlar")
    yorum = models.TextField()

    class Meta:
        verbose_name = 'yorum'
        verbose_name_plural = 'yorumlar'
    
    # def __str__(self):
    #     return self.yazan
