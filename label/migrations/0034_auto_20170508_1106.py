# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-08 02:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('label', '0033_auto_20170507_0158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='releases',
            name='label',
            field=models.CharField(choices=[('--', '--'), ('altema', 'Altema Records'), ('maltine', 'Maltine Records'), ('bunkai-kei', 'Bunkai-Kei Records'), ('trekkie trax', 'TREKKIE TRAX'), ('sense', 'SenSe'), ('flau', 'flau'), ('progressive form', 'PROGRESSIVE FOrM'), ('warp', 'Warp Records'), ('planet mu', 'Planet Mu'), ('owsla', 'OWSLA'), ('revealed', 'Revealed Recordings'), ('ghostly international', 'Ghostly International'), ("spinnin'", "Spinnin' Records"), ('wedidit', 'WEDIDIT'), ('never slept', 'Never Slept'), ('mad decent', 'Mad Decent'), ('r&s', 'R&S Records'), ('ed banger', 'Ed Banger Records'), ('brainfeeder', 'brainfeeder'), ('luckyme', 'luckyme'), ('moose', 'Moose Records'), ('anticon', 'anticon.'), ('orikami', 'Orikami Records'), ('ne', 'neRecords'), ('outlier', 'OUTLIER RECORDINGS'), ('king', 'King Deluxe'), ('gondwana', 'Gondwana Records'), ('alphaversion', 'AlphaVersion Records'), ('eklektik', 'EKLEKTIK RECORDS'), ('otographic', 'Otographic Music'), ('young', 'Young Turks'), ('n5md', 'n5MD')], default='--', max_length=500, verbose_name='Label'),
        ),
    ]
