import pymongo
from django.shortcuts import render

from .config import (mirna_collection, cancer_collection,
                     rna_collection, rcnmn_collection)


# Create your views here.
def index_view(request):
    return render(request, 'front/index.html')


def about_view(request):
    return render(request, 'front/about.html')


def link_view(request):
    return render(request, 'front/links.html')


def browse_view(request):
    req_cancer = request.GET.get('cancer', None)
    req_mirna = request.GET.get('mirna', None)
    mirna_query = mirna_collection.find()
    mirnas = []
    for mirna in mirna_query:
        mirnas.append(mirna['mirna'])
    cancers_query = cancer_collection.find()
    cancers = []
    for cancer in cancers_query:
        cancers.append(cancer['cancer'])

    data = []
    template = 'front/browse.html'
    # mirna
    if req_mirna:
        rna_query = rna_collection.find({'rna': {'$eq': req_mirna}})
        for rna in rna_query:
            temp = dict()
            temp['url'] = 'http://www.mirbase.org/cgi-bin/query.pl?terms={}'.format(rna['rna'])
            if rna['pmid'] == 'dbDEMC':
                temp['pmid_url'] = 'http://www.picb.ac.cn/dbDEMC/index.html'
            else:
                temp['pmid_url'] = 'https://www.ncbi.nlm.nih.gov/pubmed/?term={}'.format(rna['pmid'])
            temp['PMID'] = rna['pmid']
            temp['cancer'] = rna['cancer']
            temp['details'] = rna['details']
            temp['mirbase'] = 'mirbase'
            data.append(temp)

    elif req_cancer:
        cancer_query = rna_collection.find({'cancer': {'$eq': req_cancer}})
        for rna in cancer_query:
            temp = dict()
            temp['url'] = 'http://www.mirbase.org/cgi-bin/query.pl?terms={}'.format(rna['rna'])
            if rna['pmid'] == 'dbDEMC':
                temp['pmid_url'] = 'http://www.picb.ac.cn/dbDEMC/index.html'
            else:
                temp['pmid_url'] = 'https://www.ncbi.nlm.nih.gov/pubmed/?term={}'.format(rna['pmid'])
            temp['PMID'] = rna['pmid']
            temp['rna'] = rna['rna']
            temp['details'] = rna['details']
            data.append(temp)
        template = 'front/browse_cancer.html'

    return render(request, template, {
        'mirnas': mirnas,
        'cancers': cancers,
        'data': data,
    })


def rcnmc_view(request):
    req_cancer = request.GET.get('cancer', None)
    cancers_query = cancer_collection.find()
    cancers = []
    for cancer in cancers_query:
        cancers.append(cancer['cancer'])

    data = []
    template = 'front/rcnmn.html'
    if req_cancer:
        cancer_query = rcnmn_collection.find({
            'cancer': {'$eq': req_cancer}}).sort(
            'score', pymongo.DESCENDING)

        for cancer in cancer_query:
            temp = dict()
            temp['mirna'] = cancer['mirna']
            temp['score'] = cancer['score']
            data.append(temp)

    return render(request, template, {
        'cancers': cancers,
        'data': data,
    })


def kegg_view(request):
    id = request.GET.get('id', None)
    cancers = [
        'Acute myeloid leukemia',
        'Basal cell carcinoma',
        'Bladder cancer',
        'Breast cancer',
        'Chronic myeloid leukemia',
        'Colorectal cancer',
        'Endometrial cancer',
        'Glioma',
        'Melanoma',
        'Non-small cell lung cancer',
        'Pancreatic cancer',
        'Prostate cancer',
        'Renal cell carcinoma',
        'Small cell lung cancer',
        'Thyroid cancer'
    ]
    base_src = 'http://ogfcjlkt7.bkt.clouddn.com/'
    image_src = None
    cancer = None
    if id:
        cancer = cancers[int(id) - 1]
        image_src = base_src + cancer + '.png'
    return render(request, 'front/kegg.html', {
        'cancers': cancers,
        'cancer': cancer,
        'image_src': image_src
    })
