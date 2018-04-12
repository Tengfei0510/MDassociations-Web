# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LncCeRBase',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('lncrnas', models.CharField(max_length=100, verbose_name='LncRNA')),
                ('mirnas', models.CharField(max_length=100, verbose_name='MiRNA')),
                ('genes', models.CharField(max_length=100, verbose_name='Gene')),
                ('gene_ids', models.CharField(max_length=200, blank=True, verbose_name='Gene Name (All)', null=True)),
                ('pathway_name', models.TextField(blank=True, verbose_name='Pathway Name', null=True)),
                ('diseases', models.CharField(max_length=100, verbose_name='Disease/Tissue')),
                ('Description', models.TextField(blank=True, verbose_name='Description', null=True)),
                ('PubMed_ID', models.CharField(max_length=100, verbose_name='PubMed_ID')),
                ('Year', models.IntegerField(max_length=100, default=2017, verbose_name='Year')),
                ('Journal', models.CharField(max_length=100, verbose_name='Journal')),
                ('Title', models.TextField(blank=True, verbose_name='Title', null=True)),
            ],
        ),
    ]
