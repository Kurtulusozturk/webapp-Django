from django.contrib import admin

from website.models.iletisim import IletisimModel
from website.models.yorum import YorumModel
from website.models import KategoriModel,YazilarModel,MakalelerModel

# Register your models here.
# @admin.action(description='Duplicate selected item')
# def make_duplicate(modeladmin, request, queryset):
#     for item in queryset:
#         item.pk = None
#         item.save()

# Register your models here.
admin.site.register(KategoriModel)

#admindeki görünümü özelleştirmek
@admin.register(YazilarModel)
class YazilarAdmin(admin.ModelAdmin):
    search_fields = ('baslik','icerik') #arama kutusu ekler argümanlar içinde arma yapar
    list_display = [
        'baslik', 'slug','olusturulma_tarihi', 'duzenlenme_tarihi', 'yazar'
    ]

@admin.register(MakalelerModel)
class MakalelerAdmin(admin.ModelAdmin):
    search_fields = ('baslik','makale') #arama kutusu ekler argümanlar içinde arma yapar
    list_display = [
        'baslik','makale', 'slug','olusturulma_tarihi', 'duzenlenme_tarihi'
    ]

@admin.register(YorumModel)
class YorumAdmin(admin.ModelAdmin):
    list_display = ('olusturulma_tarihi','duzenlenme_tarihi',)
    # search_fields = ('yazan_username',)

@admin.register(IletisimModel)
class IletisimAdmin(admin.ModelAdmin):
    list_display = ('email','olusturulma_tarihi',)
    search_fields = ('email',)
