from django.shortcuts import render

from .config import (mirna_collection, cancer_collection,
                     rna_collection)


# Create your views here.
def index_view(request):
    return render(request, 'front/index.html')


def about_view(request):
    return render(request, 'front/about.html')


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
    print(req_cancer)
    # mirna
    if req_mirna:

        rna_query = rna_collection.find({'rna': {'$eq': req_mirna}})
        for rna in rna_query:
            temp = dict()
            if rna == 'dbDEMC':
                temp['url'] = 'http://www.mirbase.org'
            else:
                temp['url'] = 'https://www.ncbi.nlm.nih.gov/pubmed/?term={}'.format(rna['pmid'])
            temp['PMID'] = rna['pmid']
            temp['cancer'] = rna['cancer']
            temp['details'] = rna['details']
            temp['mirbase'] = 'mirbase'
            data.append(temp)
    elif req_cancer:
        cancer_query = rna_collection.find({'cancer': {'$eq': req_cancer}})
        for rna in cancer_query:
            temp = dict()
            if rna == 'dbDEMC':
                temp['url'] = 'http://www.mirbase.org'
            else:
                temp['url'] = 'https://www.ncbi.nlm.nih.gov/pubmed/?term={}'.format(rna['pmid'])
            temp['PMID'] = rna['pmid']
            temp['cancer'] = rna['cancer']
            temp['details'] = rna['details']
            temp['mirbase'] = 'mirbase'
            data.append(temp)
    print(data)
    return render(request, 'front/browse.html', {
        'mirnas': mirnas,
        'cancers': cancers,
        'data': data,
    })
