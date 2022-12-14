# Generated by Django 4.0.6 on 2022-08-15 12:35

import autoslug.fields
import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='IletisimModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=250)),
                ('isim', models.CharField(max_length=80)),
                ('soyisim', models.CharField(max_length=80)),
                ('mesaj', models.TextField()),
                ('olusturulma_tarihi', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Iletisim',
                'verbose_name_plural': 'Iletisimler',
            },
        ),
        migrations.CreateModel(
            name='KategoriModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=30)),
                ('kategori_url', models.CharField(default='#', max_length=30)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='isim', unique=True)),
            ],
            options={
                'verbose_name': 'kategori',
                'verbose_name_plural': 'kategoriler',
            },
        ),
        migrations.CreateModel(
            name='YazilarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('olusturulma_tarihi', models.DateTimeField(auto_now=True)),
                ('duzenlenme_tarihi', models.DateTimeField(auto_now=True)),
                ('resim', models.ImageField(upload_to='yazi_resimler')),
                ('baslik', models.CharField(max_length=50)),
                ('icerik', ckeditor.fields.RichTextField()),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='baslik', unique=True)),
                ('yazar', models.ForeignKey(default='1', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='yazilar', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'yazi',
                'verbose_name_plural': 'yazilar',
            },
        ),
        migrations.CreateModel(
            name='YorumModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('olusturulma_tarihi', models.DateTimeField(auto_now=True)),
                ('duzenlenme_tarihi', models.DateTimeField(auto_now=True)),
                ('yorum', models.TextField()),
                ('yazi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='yorumlar', to='website.yazilarmodel')),
            ],
            options={
                'verbose_name': 'yorum',
                'verbose_name_plural': 'yorumlar',
            },
        ),
        migrations.CreateModel(
            name='MakalelerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('olusturulma_tarihi', models.DateTimeField(auto_now=True)),
                ('duzenlenme_tarihi', models.DateTimeField(auto_now=True)),
                ('baslik', models.CharField(max_length=50)),
                ('icerik', models.FileField(upload_to='')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='baslik', unique=True)),
                ('yazar', models.ForeignKey(default='ozturkurtulus@gmail.com', on_delete=django.db.models.deletion.CASCADE, related_name='makaleler', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'makale',
                'verbose_name_plural': 'makaleler',
            },
        ),
    ]
