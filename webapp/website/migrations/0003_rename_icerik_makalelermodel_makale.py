# Generated by Django 4.0.6 on 2022-08-15 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_makalelermodel_icerik'),
    ]

    operations = [
        migrations.RenameField(
            model_name='makalelermodel',
            old_name='icerik',
            new_name='makale',
        ),
    ]
