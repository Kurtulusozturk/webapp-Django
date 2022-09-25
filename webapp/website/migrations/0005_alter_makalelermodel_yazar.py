# Generated by Django 4.0.6 on 2022-08-16 13:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0004_alter_makalelermodel_duzenlenme_tarihi_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='makalelermodel',
            name='yazar',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='makaleler', to=settings.AUTH_USER_MODEL),
        ),
    ]
